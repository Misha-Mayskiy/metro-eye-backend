from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.report import Report, ReportCategory
from app.services.file_service import file_service
from app.schemas.report import ReportRead

router = APIRouter()


@router.post("/", response_model=ReportRead)
async def create_report(
    category: ReportCategory = Form(...),
    location_info: str = Form(...),
    description: str = Form(None),
    photo: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if photo.content_type and not photo.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    photo_relative_path = await file_service.save_report_image(photo)

    new_report = Report(
        category=category,
        description=description,
        location_info=location_info,
        photo_path=photo_relative_path,
        user_id=None
    )

    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return new_report


@router.get("/", response_model=list[ReportRead])
def list_reports(db: Session = Depends(get_db)):
    return db.query(Report).all()
