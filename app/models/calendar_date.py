from sqlalchemy import Column, String, Date, Integer, ForeignKey
from database import Base

class CalendarDate(Base):
    __tablename__ = "calendar_date"

    service_id = Column(String(50), ForeignKey("calendar.service_id", ondelete="CASCADE"), primary_key=True)
    date = Column(Date, primary_key=True)
    exception_type = Column(Integer, nullable=False)
