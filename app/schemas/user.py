from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

# Base para las respuestas comunes de usuario
class UserBase(BaseModel):
    nombre: str
    email: EmailStr
    username: str
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    activo: bool = True

# Esquema para la creación de usuario, incluye la contraseña en texto plano
class UserCreate(UserBase):
    password: str  # La contraseña recibida en texto plano, debe ser encriptada luego

# Esquema de respuesta con la información básica del usuario
class UserResponse(UserBase):
    id: int
    fecha_registro: datetime

    class Config:
        from_attributes = True  # Permite mapear desde los objetos de la base de datos

# Esquema que se utiliza en la base de datos para almacenar la contraseña encriptada
class UserDB(UserResponse):
    hashed_password: str  # Guardamos la contraseña encriptada
