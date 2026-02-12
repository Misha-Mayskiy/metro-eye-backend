from sqlalchemy import Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
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

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category: Mapped[ReportCategory] = mapped_column(Enum(ReportCategory), nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    location_info: Mapped[str] = mapped_column(String, nullable=False)
    photo_path: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[ReportStatus] = mapped_column(Enum(ReportStatus), default=ReportStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    owner: Mapped["User"] = relationship("User", back_populates="reports")
