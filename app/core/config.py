from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    PROJECT_NAME: str = "MetroEye API"
    API_V1_STR: str = "/api/v1"

    # Security
    SECRET_KEY: str = "WEFVVNLKsETO8mbv4e2tFkFb8vJll2lLxhtZhg6EdwW"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 дней

    # Database
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./metro_eye.db"

    # Files
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    UPLOAD_DIR: Path = BASE_DIR / "data" / "uploads"
    DATASET_DIR: Path = BASE_DIR / "data" / "dataset"

    class Config:
        env_file = ".env"


settings = Settings()

settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
settings.DATASET_DIR.mkdir(parents=True, exist_ok=True)
