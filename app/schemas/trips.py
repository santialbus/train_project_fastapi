from pydantic import BaseModel
from typing import Optional

class TripSchema(BaseModel):
    trip_id: str
    service_id: str
    first_stop_name: Optional[str] = None
    first_stop_sequence: Optional[int] = None
    first_arrival_time: Optional[str] = None
    first_departure_time: Optional[str] = None
    last_stop_name: Optional[str] = None
    last_stop_sequence: Optional[int] = None
    last_arrival_time: Optional[str] = None
    last_departure_time: Optional[str] = None
    route_short_name: str

    class Config:
        from_attributes = True
