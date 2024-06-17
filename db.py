from flask_sqlalchemy import SQLAlchemy


# Inicjalizacja obiektu SQLAlchemy
db = SQLAlchemy()

# Model tabeli Users
class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Password = db.Column(db.String(255))

# Model tabeli Signs
class Sign(db.Model):
    SignID = db.Column(db.Integer, primary_key=True)
    SignName = db.Column(db.String(255))
    Description = db.Column(db.String(2000))
    QRCode = db.Column(db.String(255))
 #   Picture = db.Column(db.LargeBinary)

# Model tabeli Achievements
class Achievement(db.Model):
    AchievementID = db.Column(db.Integer, primary_key=True)
    AchievementName = db.Column(db.String(255))
    Description = db.Column(db.String(2000))
    Score = db.Column(db.Integer)
    Type = db.Column(db.String(255))

# Model tabeli Questions
class Question(db.Model):
    QuestionID = db.Column(db.Integer, primary_key=True)
    QuestionText = db.Column(db.String(255))

# Model tabeli Answers
class Answer(db.Model):
    AnswerID = db.Column(db.Integer, primary_key=True)
    QuestionID = db.Column(db.Integer, db.ForeignKey('question.QuestionID'))
    AnswerText = db.Column(db.String(255))
    IsCorrect = db.Column(db.Boolean)

    # Model tabeli UserCorrectAnswers
class UserCorrectAnswers(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'))
    QuestionID = db.Column(db.Integer, db.ForeignKey('question.QuestionID'))

  
    user = db.relationship('User', backref=db.backref('correct_answers', lazy=True))
    question = db.relationship('Question', backref=db.backref('correct_answers', lazy=True))


# Model tabeli ConnectingTableQuestions
class ConnectingTableQuestions(db.Model):
    SignID = db.Column(db.Integer, db.ForeignKey('sign.SignID'), primary_key=True)
    QuestionID = db.Column(db.Integer, db.ForeignKey('question.QuestionID'), primary_key=True)

# Model tabeli ConnectingTableSigns
class ConnectingTableSigns(db.Model):
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'), primary_key=True)
    SignID = db.Column(db.Integer, db.ForeignKey('sign.SignID'), primary_key=True)

# Model tabeli ConnectingTableAchievements
class ConnectingTableAchievements(db.Model):
    UserID = db.Column(db.Integer, db.ForeignKey('user.UserID'), primary_key=True)
    AchievementID = db.Column(db.Integer, db.ForeignKey('achievement.AchievementID'), primary_key=True)
