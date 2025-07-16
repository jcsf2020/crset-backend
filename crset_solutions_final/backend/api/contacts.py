import os
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud.contact import create_contact, get_contacts
from schemas.contact import ContactOut, ContactCreate
from api.auth import get_current_user
from schemas.user import UserOut

router = APIRouter()

@router.post("/", response_model=ContactOut)
async def create_new_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    # Create contact in database
    db_contact = create_contact(db=db, contact=contact)
    
    # Send email via Resend (optional - requires RESEND_API_KEY)
    try:
        resend_api_key = os.getenv("RESEND_API_KEY")
        if resend_api_key and resend_api_key != "re_demo_key":
            import resend
            resend.api_key = resend_api_key
            
            email_content = f"""
            Nova mensagem de contacto recebida:
            
            Nome: {contact.name}
            Email: {contact.email}
            Telefone: {contact.phone or 'Não fornecido'}
            
            Mensagem:
            {contact.message}
            """
            
            resend.Emails.send({
                "from": "noreply@crsetsolutions.com",
                "to": "crsetsolutions@gmail.com",
                "subject": f"Nova mensagem de {contact.name}",
                "text": email_content
            })
    except Exception as e:
        # Log error but don't fail the request
        print(f"Failed to send email: {e}")
    
    return db_contact

@router.get("/", response_model=List[ContactOut])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    contacts = get_contacts(db, skip=skip, limit=limit)
    return contacts
