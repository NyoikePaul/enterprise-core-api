import logging
from datetime import datetime, timedelta, timezone
from typing import Any
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.core.config.settings import get_settings
 
logger = logging.getLogger(__name__)
settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
 
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
 
 
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
 
 
def create_access_token(subject: str | Any, expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return jwt.encode({"exp": expire, "sub": str(subject), "type": "access"}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
 
 
def create_refresh_token(subject: str | Any) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return jwt.encode({"exp": expire, "sub": str(subject), "type": "refresh"}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
 
 
def decode_token(token: str, expected_type: str = "access") -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError as exc:
        raise ValueError("Could not validate credentials") from exc
    if payload.get("type") != expected_type:
        raise ValueError(f"Invalid token type: expected '{expected_type}', got '{payload.get('type')}'")
    return payload
