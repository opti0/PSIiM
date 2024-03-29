from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        users[username] = password  # Save user to the database (here it's a simple dictionary)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return f"Welcome, {username}!"
        else:
            error_message = "Nieprawidłowa nazwa użytkownika lub hasło. Spróbuj ponownie!"
            return render_template('login.html', error_message=error_message)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
