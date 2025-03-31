from fastapi import Depends
from pydantic import BaseModel, EmailStr, model_validator
from datetime import date, datetime
from typing import Optional
from app.models.enums.role import RoleEnum 

class UserBase(BaseModel):
    nombre: str
    email: EmailStr
    username: str
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    activo: bool = True
    role: RoleEnum = RoleEnum.user 

class UserCreate(UserBase):
    password: str  
    
class UserResponse(UserBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True  
        
class UserDB(UserResponse):
    hashed_password: str 
