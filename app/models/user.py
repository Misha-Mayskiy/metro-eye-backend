from sqlalchemy import Integer, String, Boolean
from app.core.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str | None] = mapped_column(String, nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    score: Mapped[int] = mapped_column(Integer, default=0)

    reports: Mapped[List["Report"]] = relationship("Report", back_populates="owner")
