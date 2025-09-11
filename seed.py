from app.db.database import SessionLocal, init_db
from app.models.models import User

init_db()
db = SessionLocal()

# Tabelle leeren
db.query(User).delete()
db.commit()

users = [
    User(vorname="Bruce", name="Wayne", email="brucewayne@example.com", passwort="brucewayne123"),
    User(vorname="John", name="Martsen", email="johnmarsten@example.com", passwort="johnmarsten123"),
    User(vorname="Arthur", name="Morgan", email="arthurmorgan@example.com", passwort="arthurmorgan123"),
    User(vorname="Mauro", name="Icardi", email="mauroicardi@example.com", passwort="mauroicardi123"),
    User(vorname="Victor", name="Osimhen", email="victorosimhen@example.com", passwort="victorosimhen123"),
]

db.add_all(users)
db.commit()
db.close()
