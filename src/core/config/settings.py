import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
 
 
class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env"
        ),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )
 
    PROJECT_NAME: str = "Enterprise Core API"
    VERSION: str = "1.0.0"
 
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "enterprise_db"
 
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
 
    MPESA_BASE_URL: str = "https://sandbox.safaricom.co.ke"
    MPESA_CONSUMER_KEY: str = ""
    MPESA_CONSUMER_SECRET: str = ""
    MPESA_SHORTCODE: str = "174379"
    MPESA_PASSKEY: str = ""
    MPESA_CALLBACK_URL: str = ""
    MPESA_ENVIRONMENT: str = "sandbox"
 
    ETIMS_BASE_URL: str = "https://etims-api.kra.go.ke/api/v1"
    ETIMS_DEVICE_SERIAL: str = ""
 
 
@lru_cache()
def get_settings() -> Settings:
    return Settings()
