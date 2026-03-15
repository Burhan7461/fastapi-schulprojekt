from turtle import title
from app.schemas.schemas import AppointmentItemCreate, AppointmentItemResponse, DownloadItemCreate, DownloadItemResponse, NewsItemCreate, NewsItemResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import AppointmentItem, DownloadItem, NewsItem, User
from config import DATABASE_URL, SECRET_KEY, DEBUG

# http://127.0.0.1:8000/testen
# http://localhost:8000/docs
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

@router.post("/download_items", status_code=201, response_model=DownloadItemResponse)
def create_download_item(item: DownloadItemCreate, db: Session = Depends(get_db)):
    downloadItem = DownloadItem(
        title=item.title,
        description=item.description,
        author=item.author,
        date=item.date,
        type=item.type
        )
    db.add(downloadItem)
    db.commit()
    db.refresh(downloadItem)
    return downloadItem
    
@router.get("/appointment_items")
def get_appointmentItems(db: Session = Depends(get_db)):
    print(db.bind.url)
    return db.query(AppointmentItem).all()

@router.post("/appointment_items", status_code=201, response_model=AppointmentItemResponse)
def create_appointment_item(item: AppointmentItemCreate, db: Session = Depends(get_db)):
    appointmentItem = AppointmentItem(
        title=item.title,
        description=item.description,
        date=item.date,
        location=item.location,
        type=item.mime_type,
        startDate=item.startDate,
        endDate=item.endDate,
        startTime=item.startTime,
        endTime=item.endTime,
        is_past=item.is_past
        )
    db.add(appointmentItem)
    db.commit()
    db.refresh(appointmentItem)
    return appointmentItem

@router.get("/news_items")
def get_newsItems(db: Session = Depends(get_db)):
    print(db.bind.url)
    return db.query(NewsItem).all()

@router.post("/news_items", status_code=201, response_model=NewsItemResponse)
def create_news_item(item: NewsItemCreate, db: Session = Depends(get_db)):
    newsItem = NewsItem(
        title=item.title,
        content=item.content,
        author=item.author,
        time=item.time,
        tags=item.tags,
        is_important=item.is_important,
        is_urgent=item.is_urgent,
        type=item.type
        )
    db.add(newsItem)
    db.commit()
    db.refresh(newsItem)
    return newsItem

@router.get("/testen")
def testen():
    return {"message": "Backend laeuft!"}
