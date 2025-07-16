from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServiceBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    features: Optional[str] = None
    category: str
    is_active: Optional[bool] = True

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(ServiceBase):
    pass

class ServiceOut(ServiceBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
