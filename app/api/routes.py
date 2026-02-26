from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import DownloadItem, User
from config import DATABASE_URL, SECRET_KEY, DEBUG

# http://127.0.0.1:8000/testen
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    print(db.query(User).count())
    print(db.query(DownloadItem).count())
    print(db.bind.url)
    return db.query(User).all()

@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    print(db.query(User).count())
    print(db.query(DownloadItem).count())
    print(db.bind.url)
    return db.query(DownloadItem).all()

@router.get("/news")
def testtest():
    return {"Klappt?"}

@router.get("/testen")
def hello():
    return {"message": "Backend laeuft!"}

@router.get("/config-check")
def config_check():
    return {
        "database": DATABASE_URL,
        "secret_key": SECRET_KEY,
        "debug": DEBUG
    }
