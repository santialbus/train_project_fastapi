from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Agency(Base):
    __tablename__ = "agency"

    agency_id = Column(Integer, primary_key=True)
    agency_name = Column(String(255), nullable=False)
    agency_url = Column(String(255), nullable=False)
    agency_timezone = Column(String(100), nullable=False)
    agency_lang = Column(String(10), nullable=True)
    agency_phone = Column(String(50), nullable=True)

    routes = relationship("Route", back_populates="agency")
