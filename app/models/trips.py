from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Trip(Base):
    __tablename__ = "trips"

    trip_id = Column(String(50), primary_key=True)
    route_id = Column(String(50), ForeignKey("routes.route_id", ondelete="CASCADE"))
    service_id = Column(String(50), ForeignKey("calendar.service_id", ondelete="CASCADE"))
    trip_headsign = Column(String(255), nullable=True)
    trip_short_name = Column(String(100), nullable=True)
    direction_id = Column(Integer, nullable=True)
    block_id = Column(Integer, nullable=True)
    shape_id = Column(Integer, nullable=True)
    wheelchair_accessible = Column(Integer, nullable=True)

    route = relationship("Route", back_populates="trips")
    calendar = relationship("Calendar", back_populates="trips")
    stop_times = relationship("StopTime", back_populates="trip")
