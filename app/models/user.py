from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

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
