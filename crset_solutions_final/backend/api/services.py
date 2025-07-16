from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from crud.service import get_services, get_service, create_service, update_service, delete_service
from schemas.service import ServiceOut, ServiceCreate, ServiceUpdate
from api.auth import get_current_user
from schemas.user import UserOut

router = APIRouter()

@router.get("/", response_model=List[ServiceOut])
def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    services = get_services(db, skip=skip, limit=limit)
    return services

@router.get("/{service_id}", response_model=ServiceOut)
def read_service(service_id: int, db: Session = Depends(get_db)):
    service = get_service(db, service_id=service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.post("/", response_model=ServiceOut)
def create_new_service(service: ServiceCreate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    return create_service(db=db, service=service)

@router.put("/{service_id}", response_model=ServiceOut)
def update_existing_service(service_id: int, service: ServiceUpdate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    db_service = update_service(db, service_id=service_id, service_data=service)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.delete("/{service_id}")
def delete_existing_service(service_id: int, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    service = delete_service(db, service_id=service_id)
    if service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}
