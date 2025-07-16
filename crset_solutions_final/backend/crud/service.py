from sqlalchemy.orm import Session
from models.service import Service
from schemas.service import ServiceCreate, ServiceUpdate

def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Service).filter(Service.is_active == True).offset(skip).limit(limit).all()

def get_service(db: Session, service_id: int):
    return db.query(Service).filter(Service.id == service_id).first()

def create_service(db: Session, service: ServiceCreate):
    db_service = Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def update_service(db: Session, service_id: int, service_data: ServiceUpdate):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service:
        for key, value in service_data.dict().items():
            setattr(service, key, value)
        db.commit()
        db.refresh(service)
    return service

def delete_service(db: Session, service_id: int):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service:
        service.is_active = False
        db.commit()
        db.refresh(service)
    return service
