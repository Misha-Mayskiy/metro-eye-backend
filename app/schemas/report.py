from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.report import ReportCategory


class ReportBase(BaseModel):
    category: ReportCategory
    location_info: str
    description: Optional[str] = None


class ReportCreate(ReportBase):
    pass


class ReportRead(ReportBase):
    id: int
    photo_path: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
