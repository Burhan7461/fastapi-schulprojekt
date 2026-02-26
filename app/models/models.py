from datetime import datetime
from os import name
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
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

class Lehrer(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Klasse(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Raum(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Fach(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)

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
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    location = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)
    is_past = Column(Boolean, default=False)

class NewsItem(Base):
    __tablename__ = "news_items"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.utcnow, nullable=False)
    tags = Column(Text, nullable=True)
    is_important = Column(Boolean, default=False)
    is_urgent = Column(Boolean, default=False)
    type = Column(String, nullable=False)
