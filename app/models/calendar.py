from sqlalchemy import Column, String, Boolean, Date
from sqlalchemy.orm import relationship
from database import Base

class Calendar(Base):
    __tablename__ = "calendar"

    service_id = Column(String(50), primary_key=True)
    monday = Column(Boolean, nullable=False)
    tuesday = Column(Boolean, nullable=False)
    wednesday = Column(Boolean, nullable=False)
    thursday = Column(Boolean, nullable=False)
    friday = Column(Boolean, nullable=False)
    saturday = Column(Boolean, nullable=False)
    sunday = Column(Boolean, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    trips = relationship("Trip", back_populates="calendar")
