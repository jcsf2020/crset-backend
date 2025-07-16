from sqlalchemy.orm import Session
from models.contact import Contact
from schemas.contact import ContactCreate

def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contact).offset(skip).limit(limit).all()
