from db import *
import fillDB
import secrets
import os
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random
from flask import Flask, render_template, request, redirect, url_for, session, flash



# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Ustawienie sekretnego klucza dla sesji, generowane losowo za każdym razem, gdy aplikacja się uruchamia
app.secret_key = secrets.token_hex(16)

# Konfiguracja bazy danych
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'database.db')
db.init_app(app)


# Utworzenie wszystkich tabel w bazie danych, jeśli nie istnieją
with app.app_context():
    db.create_all()
    fillDB.fill(db) #dodanie znaków, pytań i osiągnięć, jeśli nie istnieją

# Główna strona aplikacji
@app.route('/')
def index():
    # Wyświetlanie strony głównej z aktualnie zalogowanym użytkownikiem
    return render_template('index.html', current_user=session.get('current_user'))

# Strona i logika rejestracji użytkownika
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Pobieranie danych z formularza
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Sprawdzenie, czy użytkownik już istnieje w bazie danych
        existing_user = User.query.filter_by(Name=username).first()
        if existing_user:
            error_message = "Użytkownik o tej nazwie już istnieje. Proszę wybrać inną nazwę."
            return render_template('register.html', error_message=error_message)
        existing_user = User.query.filter_by(Email=email).first()
        if existing_user:
            error_message = "Użytkownik o podanym adresie email już istnieje. Może chcesz się <a href='/login'>zalogować</a>?"
            return render_template('register.html', error_message=error_message)

        # Rejestracja nowego użytkownika
        new_user = User(Name=username, Password=password, Email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Strona i logika logowania użytkownika
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Pobieranie danych z formularza
        username = request.form['username']
        password = request.form['password']

        # Sprawdzenie, czy dane logowania są poprawne
        user = User.query.filter_by(Name=username, Password=password).first()
        if user and user.Password == password:
            print("Zalogowano")
            # Ustawienie sesji użytkownika
            session['user_id'] = user.UserID
            session['current_user'] = user.Name
            return redirect(url_for('index'))
        else:
            error_message = "Nieprawidłowa nazwa użytkownika lub hasło. Spróbuj ponownie!"
            return render_template('login.html', error_message=error_message)
    return render_template('login.html')


# Trasa odpowiedzialna za wylogowanie użytkownika
@app.route('/logout', methods=['GET'])
def logout():
    session.clear()  # Usunięcie wszystkich danych z sesji
    return redirect(url_for('login'))  # Przekierowanie do strony logowania

# Trasa do wyświetlania osiągnięć użytkownika
@app.route('/achievements')
def achievements():
    current_user = session.get('current_user')  # Pobranie aktualnie zalogowanego użytkownika z sesji
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Przekierowanie do logowania, jeśli użytkownik nie jest zalogowany

    user_id = session['user_id']  # Pobranie ID zalogowanego użytkownika

    # Pobranie osiągnięć użytkownika z bazy danych
    user_achievements = db.session.query(Achievement).join(ConnectingTableAchievements).filter(
        ConnectingTableAchievements.UserID == user_id
    ).all()

    # Wyświetlenie strony z osiągnięciami
    return render_template('achievements.html', achievements=user_achievements, current_user=current_user)

# Trasa odpowiedzialna za skanowanie kodów QR
@app.route('/qr_scanning', methods=['GET', 'POST'])
def qr_scanning():
    error_message = None  # Zmienna na wiadomości o błędach
    success_message = None  # Zmienna na wiadomości o sukcesie
    found_sign = None  # Znaleziony znak

    if 'user_id' not in session:
        return redirect(url_for('login'))  # Przekierowanie do logowania, jeśli użytkownik nie jest zalogowany

    user_id = session['user_id']
    current_user = session.get('current_user')

    if request.method == 'POST':
        code = request.form['code']  # Pobranie kodu z formularza

        found_sign = Sign.query.filter_by(QRCode=code).first()
        if found_sign:
            existing_connection = ConnectingTableSigns.query.filter_by(UserID=user_id, SignID=found_sign.SignID).first()
            if not existing_connection:
                new_connection = ConnectingTableSigns(UserID=user_id, SignID=found_sign.SignID)
                db.session.add(new_connection)
                db.session.commit()
                success_message = "Gratulacje! Znalazłeś nowy znak!"
                check_and_award_achievements(user_id)  # Sprawdzenie i przyznanie osiągnięć
            else:
                error_message = "Ten znak został już przez ciebie znaleziony."
        else:
            error_message = "Nie znaleziono znaku o podanym kodzie QR."

    return render_template('qr_scanning.html', error_message=error_message, success_message=success_message, found_sign=found_sign, current_user=current_user)

# Funkcja sprawdzająca i przyznająca osiągnięcia
def check_and_award_achievements(user_id):
    sign_count = db.session.query(func.count(ConnectingTableSigns.SignID)).filter(ConnectingTableSigns.UserID == user_id).scalar()
    thresholds = {1: 1, 2: 5, 3: 10, 4: 20, 5: 50}  # Próg osiągnięć

    user_achievements = db.session.query(ConnectingTableAchievements.AchievementID).filter(ConnectingTableAchievements.UserID == user_id).all()
    user_achievements_ids = {Achievement.AchievementID for Achievement in user_achievements}

    for achievement_id, threshold in thresholds.items():
        if sign_count >= threshold and achievement_id not in user_achievements_ids:
            new_award = ConnectingTableAchievements(UserID=user_id, AchievementID=achievement_id)
            db.session.add(new_award)
            print(f"Przyznano osiągnięcie o ID: {achievement_id}")

    db.session.commit()  # Zatwierdzenie transakcji w bazie danych


# Trasa do wyświetlania znalezionych znaków przez użytkownika
@app.route('/found_signs')
def found_signs():
    current_user = session.get('current_user')  # Pobranie bieżącego użytkownika z sesji
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Przekierowanie do logowania jeśli użytkownik nie jest zalogowany

    user_id = session['user_id']  # Pobranie ID użytkownika z sesji

    # Zapytanie do bazy danych o znaki znalezione przez użytkownika
    found_signs = db.session.query(Sign).join(ConnectingTableSigns).filter(
        ConnectingTableSigns.UserID == user_id
    ).all()

    # Renderowanie strony z listą znalezionych znaków
    return render_template('found_signs.html', found_signs=found_signs, current_user=current_user)

# Trasa do zarządzania ustawieniami użytkownika
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    current_user = session.get('current_user')
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        user = User.query.filter_by(UserID=user_id).first()  # Pobranie danych użytkownika

        if password != confirm_password:
            flash('Hasła nie są identyczne.', 'error')  # Komunikat o błędzie
            return redirect(url_for('settings'))

        # Aktualizacja danych użytkownika
        if username:
            user.Name = username
        if email:
            user.Email = email
        if password:
            user.Password = password

        db.session.commit()  # Zapisanie zmian w bazie danych

        flash('Zmiany zostały zapisane.', 'success')  # Komunikat o sukcesie
        return redirect(url_for('settings'))

    current_email = User.query.filter_by(Name=current_user).first().Email  # Pobranie aktualnego emaila użytkownika
    return render_template('settings.html', current_user=current_user, current_email=current_email)

# Trasa do profilu użytkownika
@app.route('/profile')
def profile():
    current_user = session.get('current_user')
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Przekierowanie do logowania jeśli użytkownik nie jest zalogowany

    user_id = session['user_id']
    user = User.query.filter_by(UserID=user_id).first()  # Pobranie danych użytkownika z bazy

    # Liczenie znalezionych znaków i osiągnięć
    found_signs_count = ConnectingTableSigns.query.filter_by(UserID=user_id).count()
    achievements_count = ConnectingTableAchievements.query.filter_by(UserID=user_id).count()

    # Renderowanie strony profilu z podanymi danymi
    return render_template('profile.html', user=user, found_signs_count=found_signs_count, achievements_count=achievements_count, current_user=current_user)



# Definiowanie trasy do obsługi quizu, obsługiwane są metody GET i POST
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    current_user = session.get('current_user')  # Pobranie aktualnego użytkownika z sesji
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Przekierowanie do logowania, jeśli użytkownik nie jest zalogowany

    user_id = session['user_id']  # Pobranie identyfikatora użytkownika z sesji
    
    if request.method == 'POST':  # Obsługa żądania typu POST (gdy użytkownik przesyła odpowiedzi)
        user_answers = request.form.to_dict()  # Pobranie odpowiedzi użytkownika z formularza
        
        if not user_answers:
            return redirect(url_for('quiz'))  # Jeśli brak odpowiedzi, przekieruj do quizu ponownie
        
        question_ids = session.get('question_ids', [])  # Pobranie identyfikatorów pytań z sesji
        questions = Question.query.filter(Question.QuestionID.in_(question_ids)).all()  # Pobranie pytań na podstawie ID
        
        correct_answers = {}  # Słownik do przechowywania poprawnych odpowiedzi
        for question in questions:
            correct_answer = Answer.query.filter_by(QuestionID=question.QuestionID, IsCorrect=True).first()
            if correct_answer:
                correct_answers[str(question.QuestionID)] = str(correct_answer.AnswerID)  # Zapis poprawnej odpowiedzi
        
        results = {}  # Słownik do przechowywania wyników odpowiedzi użytkownika
        for key, value in user_answers.items():
            question_id = key.replace("question", "")
            if question_id in correct_answers:
                results[int(question_id)] = {
                    'correct': correct_answers[question_id] == value,
                    'selected': int(value)
                }

                # Zapisanie poprawnej odpowiedzi do bazy danych
                if results[int(question_id)]['correct']:
                    new_correct_answer = UserCorrectAnswers(UserID=user_id, QuestionID=int(question_id))
                    db.session.add(new_correct_answer)
                    db.session.commit()

        available_questions = [q for q in question_ids if q not in session.get('answered_correctly', [])]

        # Logika do decydowania, które pytania mają być wyświetlone użytkownikowi
        if len(available_questions) < 5:
            if not available_questions:
                return redirect(url_for('congratulations'))  # Przekierowanie na stronę gratulacji jeśli brak pytań
            questions = Question.query.filter(Question.QuestionID.in_(available_questions)).all()
        else:
            questions = Question.query.filter(Question.QuestionID.in_(available_questions[:5])).all()

        for question in questions:
            question.answers = Answer.query.filter_by(QuestionID=question.QuestionID).all()  # Pobranie odpowiedzi dla pytań

        return render_template('quiz.html', questions=questions, results=results, current_user=current_user)
    
    else:  # Obsługa żądania typu GET (wyświetlenie formularza z pytaniami)
        user_id = session.get('user_id')
        available_question_ids = [q.QuestionID for q in Question.query.all()]
        answered_correctly = [q.QuestionID for q in UserCorrectAnswers.query.filter_by(UserID=user_id).all()]
        available_questions = [q for q in available_question_ids if q not in answered_correctly]

        if len(available_questions) < 5:
            if not available_questions:
                return redirect(url_for('congratulations'))
            question_objects = Question.query.filter(Question.QuestionID.in_(available_questions)).all()
        else:
            questions = random.sample(available_questions, 5)
            question_objects = Question.query.filter(Question.QuestionID.in_(questions)).all()

        session['question_ids'] = [q.QuestionID for q in question_objects]  # Zapis identyfikatorów pytań do sesji

        for question in question_objects:
            question.answers = Answer.query.filter_by(QuestionID=question.QuestionID).all()  # Pobranie odpowiedzi dla pytań

        return render_template('quiz.html', questions=question_objects, current_user=current_user)  # Wyświetlenie quizu

# Trasa do strony z gratulacjami po zakończeniu quizu
@app.route('/congratulations')
def congratulations():
    current_user = session.get('current_user')
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Przekierowanie do logowania

    user_id = session['user_id']
    return render_template('congratulations.html', current_user=current_user)  # Wyświetlenie strony z gratulacjami

# Trasa do strony FAQ
@app.route('/faq')
def faq():
    return render_template('faq.html')  # Wyświetlenie strony FAQ

# Trasa do strony O nas
@app.route('/about')
def about():
    return render_template('about.html')  # Wyświetlenie strony O nas

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)  
