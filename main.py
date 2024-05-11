from flask import Flask, render_template, request, redirect, url_for, session
from db import *
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# Konfiguracja połączenia z bazą danych
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

# Tworzenie tablic w bazie danych
with app.app_context():
    db.create_all()

# Dummy user database
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Sprawdzamy, czy użytkownik już istnieje w bazie danych
        existing_user = User.query.filter_by(Name=username).first()
        if existing_user:
            error_message = "Użytkownik o tej nazwie już istnieje. Proszę wybrać inną nazwę."
            return render_template('register.html', error_message=error_message)
        # Jeśli użytkownik nie istnieje, dodajemy go do bazy danych
        new_user = User(Name=username, Password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(Name=username, Password=password).first()
        if user and user.Password == password:
            session['user_id'] = user.UserID
            return redirect(url_for('index'))
        else:
            error_message = "Nieprawidłowa nazwa użytkownika lub hasło. Spróbuj ponownie!"
            return render_template('login.html', error_message=error_message)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
