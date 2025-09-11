from os import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
