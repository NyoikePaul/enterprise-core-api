import os
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str = "Enterprise Core API"

    # Database
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "db"  # Default for Docker
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "enterprise_db"

    # JWT Settings
    SECRET_KEY: str = "supersecretkeychangethisinproduction2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"
        )
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    # Allow overriding host for local migrations (set to localhost)
    settings = Settings()
    if os.getenv("ALEMBIC_HOST_OVERRIDE") == "localhost":
        settings.POSTGRES_HOST = "localhost"
    return settings
