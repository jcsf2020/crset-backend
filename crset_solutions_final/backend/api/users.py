from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from crud.user import get_users
from schemas.user import UserOut
from api.auth import get_current_user

router = APIRouter()

@router.get("/", response_model=List[UserOut])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    users = get_users(db, skip=skip, limit=limit)
    return users
