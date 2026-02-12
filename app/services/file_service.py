import uuid
import shutil
from pathlib import Path
from fastapi import UploadFile
from app.core.config import settings


class FileService:
    @staticmethod
    async def save_report_image(file: UploadFile) -> str:
        file_extension = Path(str(file.filename)).suffix
        unique_filename = f"{uuid.uuid4()}{file_extension}"

        file_path = settings.UPLOAD_DIR / unique_filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return f"data/uploads/{unique_filename}"


file_service = FileService()
