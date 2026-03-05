from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import AppointmentItem, DownloadItem, NewsItem, User
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
    print(db.bind.url)
    return db.query(User).all()

@router.get("/download_items")
def get_items(db: Session = Depends(get_db)):
    print(db.bind.url)
    return db.query(DownloadItem).all()

@router.get("/appointment_items")
def get_appointmentItems(db: Session = Depends(get_db)):
    print(db.bind.url)
    return db.query(AppointmentItem).all()

@router.get("/news_items")
def get_newsItems(db: Session = Depends(get_db)):
    print(db.bind.url)
    return db.query(NewsItem).all()

@router.get("/testen")
def testen():
    return {"message": "Backend laeuft!"}
