from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.core.database import Base


class ReportStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class ReportCategory(str, enum.Enum):
    SEAT = "Сиденье"
    HANDRAIL = "Поручень"
    WALL_DOOR = "Стена/дверь"
    FLOOR = "Пол"
    GRAFFITI = "Граффити"
    GLASS = "Стекло"
    OTHER = "Другое"


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(Enum(ReportCategory), nullable=False, index=True)
    description = Column(String)
    location_info = Column(String, nullable=False)
    photo_path = Column(String)
    status = Column(Enum(ReportStatus), default=ReportStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="reports")
