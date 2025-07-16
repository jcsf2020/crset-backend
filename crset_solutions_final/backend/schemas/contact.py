from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class ContactBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    message: str

class ContactCreate(ContactBase):
    pass

class ContactOut(ContactBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
