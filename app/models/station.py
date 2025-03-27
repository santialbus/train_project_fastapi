from pydantic import BaseModel
from typing import Optional

class Station(BaseModel):
    codigo: str
    latitud: Optional[float]
    longitud: Optional[float]
    direccion: Optional[str]
    cp: Optional[str]
    poblacion: Optional[str]
    provincia: Optional[str]
    pais: Optional[str]

    class Config:
        extra = "ignore"
