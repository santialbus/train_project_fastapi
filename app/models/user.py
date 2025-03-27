from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

class UserBase(BaseModel):
    nombre: str
    email: EmailStr
    username: str
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    activo: bool = True

class UserCreate(UserBase):
    password: str  # Se recibe en texto plano, pero luego se debe encriptar

class UserResponse(UserBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True  # Para que funcione con ORMs

class UserDB(UserResponse):
    hashed_password: str  # Guardamos la contraseña encriptada


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    telefono = Column(String, nullable=True)
    fecha_nacimiento = Column(Date, nullable=True)
    activo = Column(Boolean, default=True)
    hashed_password = Column(String)
    fecha_registro = Column(DateTime, server_default=func.now())
