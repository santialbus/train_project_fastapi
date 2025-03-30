from sqlalchemy.orm import Session
from app.models.user import User
from app.models.favorite_station import FavoriteStation
from app.schemas.favorite_station import FavoriteStationCreate
from fastapi import HTTPException

class FavoriteStationService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_favorite_station(self, user_id: int, favorite_station: FavoriteStationCreate) -> FavoriteStation:
        # Verificar si el usuario existe
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Crear la nueva estación favorita
        new_favorite_station = FavoriteStation(
            user_id=user_id,
            codigo=favorite_station.codigo,
            latitud=favorite_station.latitud,
            longitud=favorite_station.longitud,
            direccion=favorite_station.direccion,
            cp=favorite_station.cp,
            poblacion=favorite_station.poblacion,
            provincia=favorite_station.provincia,
            pais=favorite_station.pais
        )

        # Agregar a la base de datos y hacer commit
        self.db.add(new_favorite_station)
        self.db.commit()
        self.db.refresh(new_favorite_station)
        
        return new_favorite_station

    def get_favorite_stations_by_user_id(self, user_id: int) -> list[FavoriteStation]:
        # Obtener estaciones favoritas del usuario
        favorite_stations = self.db.query(FavoriteStation).filter(FavoriteStation.user_id == user_id).all()
        
        if not favorite_stations:
            raise HTTPException(status_code=404, detail="No favorite stations found for this user")
        
        return favorite_stations
