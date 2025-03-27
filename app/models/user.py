from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

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
