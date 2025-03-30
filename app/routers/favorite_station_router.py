from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.services.favorite_station_service import FavoriteStationService
from app.schemas.favorite_station import FavoriteStationCreate, FavoriteStation
from app.database import get_db

router = APIRouter()

@router.post("/users/{user_id}/favorite_stations/", response_model=FavoriteStation)
async def add_favorite_station(
    user_id: int,
    favorite_station: FavoriteStationCreate,
    db: Session = Depends(get_db),
):
    # Llamamos al service para agregar la estación favorita
    favorite_station_service = FavoriteStationService(db)
    created_favorite_station = favorite_station_service.create_favorite_station(user_id, favorite_station)
    
    return created_favorite_station

@router.get("/users/{user_id}/favorite_stations/", response_model=List[FavoriteStation])
async def get_favorite_stations(
    user_id: int,
    db: Session = Depends(get_db),
):
    # Llamamos al service para obtener las estaciones favoritas del usuario
    favorite_station_service = FavoriteStationService(db)
    favorite_stations = favorite_station_service.get_favorite_stations_by_user_id(user_id)
    
    return favorite_stations
