from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Route(Base):
    __tablename__ = "routes"

    route_id = Column(String(50), primary_key=True)
    agency_id = Column(Integer, ForeignKey("agency.agency_id", ondelete="CASCADE"))
    route_short_name = Column(String(100), nullable=False)
    route_long_name = Column(String(255), nullable=True)
    route_desc = Column(Text, nullable=True)
    route_type = Column(Integer, nullable=False)
    route_url = Column(String(255), nullable=True)
    route_color = Column(String(7), nullable=True)
    route_text_color = Column(String(7), nullable=True)

    agency = relationship("Agency", back_populates="routes")
    trips = relationship("Trip", back_populates="route")
