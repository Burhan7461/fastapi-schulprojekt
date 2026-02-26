from app.db.database import SessionLocal, init_db
from app.models.models import User, DownloadItem
import traceback

init_db()
db = SessionLocal()

# Tabelle leeren
db.query(User).delete()
db.query(DownloadItem).delete()
db.commit()

users = [
    User(vorname="Bruce", name="Wayne", email="brucewayne@example.com", passwort="brucewayne123"),
    User(vorname="John", name="Martsen", email="johnmarsten@example.com", passwort="johnmarsten123"),
    User(vorname="Arthur", name="Morgan", email="arthurmorgan@example.com", passwort="arthurmorgan123"),
    User(vorname="Mauro", name="Icardi", email="mauroicardi@example.com", passwort="mauroicardi123"),
    User(vorname="Victor", name="Osimhen", email="victorosimhen@example.com", passwort="victorosimhen123"),
]

items = [
    DownloadItem(title="Testitem", description="Testitem", author="Testitem", mime_type="Testitem"),
    DownloadItem(title="Testitem", description="Testitem", author="Testitem", mime_type="Testitem"),
]

print("Before add_all - new:", [type(o).__name__ for o in db.new])
db.add_all(users)
print("After add users - new:", [type(o).__name__ for o in db.new])
db.add_all(items)
print("After add items - new:", [type(o).__name__ for o in db.new])

try:
    db.commit()
    print("Commit succeeded")
except Exception:
    print("Commit failed:")
    traceback.print_exc()
    db.rollback()

print("Counts after commit -> Users:", db.query(User).count(), "Items:", db.query(DownloadItem).count())
# Show raw rows for troubleshooting
print("Users rows:", [ (u.id, u.vorname, u.email) for u in db.query(User).all() ])
print("Items rows:", [ (i.id, i.title, i.author, i.mime_type) for i in db.query(DownloadItem).all() ])

db.close()
