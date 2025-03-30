from pydantic import BaseModel
from typing import Optional

class FavoriteStationBase(BaseModel):
    codigo: str
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    direccion: Optional[str] = None
    cp: Optional[str] = None
    poblacion: Optional[str] = None
    provincia: Optional[str] = None
    pais: Optional[str] = None

    class Config:
        orm_mode = True

class FavoriteStationCreate(FavoriteStationBase):
    user_id: int  # ID del usuario que agrega la estación favorita
