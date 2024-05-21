from flask import Flask, render_template, request, redirect, url_for, session
from db import *
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# Konfiguracja połączenia z bazą danych
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Sign': Sign,
        'Achievement': Achievement,
        'Question': Question,
        'Answer': Answer,
        'ConnectingTableQuestions': ConnectingTableQuestions,
        'ConnectingTableSigns': ConnectingTableSigns,
        'ConnectingTableAchievements': ConnectingTableAchievements
    }



# Tworzenie tablic w bazie danych
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', current_user=session.get('current_user'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Sprawdzamy, czy użytkownik już istnieje w bazie danych
        existing_user = User.query.filter_by(Name=username).first()
        if existing_user:
            error_message = "Użytkownik o tej nazwie już istnieje. Proszę wybrać inną nazwę."
            return render_template('register.html', error_message=error_message)
        existing_user = User.query.filter_by(Email=email).first()
        if existing_user:
            error_message = "Użytkownik o podanym adresie email już istnieje. Może chcesz się <a href='/login'>zalogować</a>?"
            return render_template('register.html', error_message=error_message)
        # Jeśli użytkownik nie istnieje, dodajemy go do bazy danych
        new_user = User(Name=username, Password=password, Email = email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request)
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(Name=username, Password=password).first()
        if user and user.Password == password:
            print("Zalogowano")
            session['user_id'] = user.UserID
            session['current_user'] = user.Name
            return redirect(url_for('index'))
        else:
            error_message = "Nieprawidłowa nazwa użytkownika lub hasło. Spróbuj ponownie!"
            return render_template('login.html', error_message=error_message)
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/achievements')
def achievements():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    
    # Pobieranie osiągnięć użytkownika
    user_achievements = db.session.query(Achievement).join(ConnectingTableAchievements).filter(
        ConnectingTableAchievements.UserID == user_id
    ).all()

    return render_template('achievements.html', achievements=user_achievements)


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
