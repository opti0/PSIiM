from main import db, app, Achievement


# Przykładowe osiągnięcia
achievements = [
    Achievement(AchievementName="Pierwsze logowanie", Description="Zaloguj się po raz pierwszy", Score=10, Type="Logowanie"),
    Achievement(AchievementName="Super Skaner", Description="Zeskanuj 10 kodów QR", Score=50, Type="Skanowanie"),
    Achievement(AchievementName="Quiz Mistrz", Description="Rozwiąż 5 quizów z wynikiem powyżej 80%", Score=100, Type="Quiz"),
    Achievement(AchievementName="Znakoman", Description="Znajdź wszystkie znaki", Score=200, Type="Znaki"),
    Achievement(AchievementName="Ustawienia Ekspert", Description="Skonfiguruj swoje konto w ustawieniach", Score=20, Type="Ustawienia")
]

# Dodawanie danych do bazy
with app.app_context():
    db.session.bulk_save_objects(achievements)
    db.session.commit()

print("Przykładowe osiągnięcia zostały dodane do bazy danych.")
