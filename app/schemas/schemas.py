from datetime import datetime
from typing import Optional, List
from unittest.mock import Base
from pydantic import BaseModel, EmailStr

# --- DownloadItem ---
class DownloadItemCreate(BaseModel):
    title: str
    description: str
    author: str
    date: datetime
    type: str

class DownloadItemResponse(BaseModel):
    id: int
    title: str
    description: str
    author: str
    date: datetime
    type: str

    model_config = {"from_attributes": True}

# --- User ---
class UserCreate(BaseModel):
    vorname: str
    name: str
    email: str

class UserResponse(BaseModel):
    vorname: str
    name: str
    email: str

    model_config = {"from_attributes": True}

# --- AppointmentItem ---
class AppointmentItemCreate(BaseModel):
    title: str
    description: str
    date: datetime
    location: str
    mime_type: str
    startDate: datetime
    endDate: datetime
    startTime: datetime
    endTime: datetime
    is_past: str

class AppointmentItemResponse(BaseModel):
    id: int
    title: str
    description: str
    date: datetime
    location: str
    mime_type: str
    startDate: datetime
    endDate: datetime
    startTime: datetime
    endTime: datetime
    is_past: str

    model_config = {"from_attributes": True}

# --- NewsItem ---
class NewsItemCreate(BaseModel):
    title: str
    content: str
    author: str
    time: datetime
    tags: List[str]
    is_important: bool
    is_urgent: bool
    type: str

class NewsItemResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str
    time: datetime
    tags: List[str]
    is_important: bool
    is_urgent: bool
    type: str

    model_config = {"from_attributes": True}
