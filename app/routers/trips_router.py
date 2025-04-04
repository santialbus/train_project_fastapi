from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.trip_service import get_trips_from_alicante
from app.schemas.trips import TripSchema
from typing import List

router = APIRouter(prefix="/trips", tags=["Trips"])

@router.get("/", response_model=List[TripSchema])
def get_trips(date: str, db: Session = Depends(get_db)):
    return get_trips_from_alicante(db, date)
