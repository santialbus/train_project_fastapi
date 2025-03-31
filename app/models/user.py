# app/models/user.py
from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, Enum
from sqlalchemy.sql import func
from app.models.base import Base  # Importamos Base desde aquí
from sqlalchemy.orm import relationship
from app.models.enums.role import RoleEnum 

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
    role = Column(Enum(RoleEnum), default=RoleEnum.user) 

    favorite_stations = relationship("FavoriteStation", back_populates="user")
