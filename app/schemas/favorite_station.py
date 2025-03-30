from pydantic import BaseModel
from typing import Optional

# Modelo para la respuesta de la estación favorita
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

# Modelo para la creación de una estación favorita
class FavoriteStationCreate(FavoriteStationBase):
    pass

# Modelo para la respuesta al consultar las estaciones favoritas de un usuario
class FavoriteStation(FavoriteStationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
