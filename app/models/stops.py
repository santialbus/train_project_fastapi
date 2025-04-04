from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Stop(Base):
    __tablename__ = "stops"

    stop_id = Column(Integer, primary_key=True)
    stop_code = Column(String(50), nullable=True)
    stop_name = Column(String(255), nullable=False)
    stop_desc = Column(Text, nullable=True)
    stop_lat = Column(String(100), nullable=True)
    stop_lon = Column(String(100), nullable=True)
    zone_id = Column(Integer, nullable=True)
    stop_url = Column(String(255), nullable=True)
    location_type = Column(Integer, nullable=True)
    parent_station = Column(Integer, nullable=True)
    stop_timezone = Column(String(50), nullable=True)
    wheelchair_boarding = Column(Integer, nullable=True)

    stop_times = relationship("StopTime", back_populates="stop")
