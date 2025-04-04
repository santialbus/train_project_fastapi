from sqlalchemy import Column, String, Integer, Time, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StopTime(Base):
    __tablename__ = "stop_times"

    trip_id = Column(String(50), ForeignKey("trips.trip_id", ondelete="CASCADE"), primary_key=True)
    stop_sequence = Column(Integer, primary_key=True)
    stop_id = Column(Integer, ForeignKey("stops.stop_id", ondelete="CASCADE"))
    arrival_time = Column(Time, nullable=False)
    departure_time = Column(Time, nullable=False)
    stop_headsign = Column(String, nullable=True)
    pickup_type = Column(Integer, nullable=True)
    drop_off_type = Column(Integer, nullable=True)
    shape_dist_traveled = Column(Float, nullable=True)

    trip = relationship("Trip", back_populates="stop_times")
    stop = relationship("Stop", back_populates="stop_times")
