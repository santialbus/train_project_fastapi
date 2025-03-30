from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.models.base import Base  # Importamos Base desde aquí

class FavoriteStation(Base):
    __tablename__ = "favorite_stations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # Relación con el usuario
    codigo = Column(String, index=True)  # Código único de la estación
    latitud = Column(Float, nullable=True)
    longitud = Column(Float, nullable=True)
    direccion = Column(String, nullable=True)
    cp = Column(String, nullable=True)
    poblacion = Column(String, nullable=True)
    provincia = Column(String, nullable=True)
    pais = Column(String, nullable=True)

    user = relationship("User", back_populates="favorite_stations")  # Relación con el usuario
