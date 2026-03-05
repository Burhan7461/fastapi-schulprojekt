from datetime import datetime
from app.db.database import SessionLocal, init_db
from app.models.models import AppointmentItem, NewsItem, User, DownloadItem
import traceback

init_db()
db = SessionLocal()

# Tabelle leeren
db.query(User).delete()
db.query(DownloadItem).delete()
db.query(AppointmentItem).delete()
db.query(NewsItem).delete()
db.commit()

users = [
    User(vorname="Bruce", name="Wayne", email="brucewayne@example.com", passwort="brucewayne123"),
    User(vorname="John", name="Martsen", email="johnmarsten@example.com", passwort="johnmarsten123"),
    User(vorname="Arthur", name="Morgan", email="arthurmorgan@example.com", passwort="arthurmorgan123"),
    User(vorname="Mauro", name="Icardi", email="mauroicardi@example.com", passwort="mauroicardi123"),
    User(vorname="Victor", name="Osimhen", email="victorosimhen@example.com", passwort="victorosimhen123"),
]

downloadItems = [
    DownloadItem(title="Testitem", description="Testitem", author="Testitem", date=datetime.utcnow(), type="Formulare"),
    DownloadItem(title="Testitem", description="Testitem", author="Testitem", date=datetime.utcnow(), type="Formulare"),
    DownloadItem(title="Testitem", description="Testitem", author="Testitem", date=datetime.utcnow(), type="Formulare"),
]

appointmentItems = [
    AppointmentItem(title="Testitem", description="Testitem", date=datetime.utcnow(), location="BK-Witten", type="Blocktzeiten", startDate=datetime.utcnow(), endDate=datetime.utcnow(), startTime=datetime.utcnow(), endTime=datetime.utcnow(), is_past=False),
    AppointmentItem(title="Testitem", description="Testitem", date=datetime.utcnow(), location="BK-Witten", type="Blocktzeiten", startDate=datetime.utcnow(), endDate=datetime.utcnow(), startTime=datetime.utcnow(), endTime=datetime.utcnow(), is_past=False),
    AppointmentItem(title="Testitem", description="Testitem", date=datetime.utcnow(), location="BK-Witten", type="Blocktzeiten", startDate=datetime.utcnow(), endDate=datetime.utcnow(), startTime=datetime.utcnow(), endTime=datetime.utcnow(), is_past=False),
]

newsItems = [
    NewsItem(title="Neue Cafeteria Zeiten",
             content="Die Cafeteria oeffnet jetzt laenger.",
             author="Verwaltung",
             time=datetime.utcnow(),
             tags=["Allgemein"],
             type="Allgemein",
             is_important=False,
             is_urgent=False),
]

print("Before add_all - new:", [type(o).__name__ for o in db.new])
db.add_all(users)
print("After add users - new:", [type(o).__name__ for o in db.new])
db.add_all(downloadItems)
print("After add downloadItems - new:", [type(o).__name__ for o in db.new])
db.add_all(appointmentItems)
print("After add appointmentItems - new:", [type(o).__name__ for o in db.new])
db.add_all(newsItems)
print("After add newsItems - new:", [type(o).__name__ for o in db.new])

try:
    db.commit()
    print("Commit succeeded")
except Exception:
    print("Commit failed:")
    traceback.print_exc()
    db.rollback()

db.close()
