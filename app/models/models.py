from datetime import datetime
from os import name
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    vorname = Column(String)
    name = Column(String)
    email = Column(String)
    passwort = Column(String)

class DownloadItem(Base):
    __tablename__ = "download_items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    author = Column(String)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    type = Column(String)

class AppointmentItem(Base):
    __tablename__ = "appointment_items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    location = Column(String)
    type = Column(String)
    startDate = Column(DateTime, default=datetime.utcnow, nullable=False)
    endDate = Column(DateTime, default=datetime.utcnow, nullable=False)
    startTime = Column(DateTime, default=datetime.utcnow, nullable=False)
    endTime = Column(DateTime, default=datetime.utcnow, nullable=False)
    is_past = Column(Boolean)

class NewsItem(Base):
    __tablename__ = "news_items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    author = Column(String)
    time = Column(DateTime, default=datetime.utcnow, nullable=False)
    tags = Column(JSON, default=list, nullable=True)
    is_important = Column(Boolean)
    is_urgent = Column(Boolean)
    type = Column(String)
