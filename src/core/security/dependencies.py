import logging
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
 
from src.core.database import get_db
from src.core.security import decode_token
from src.models.user import User
 
logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
 
 
async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token, expected_type="access")
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except ValueError as exc:
        logger.warning("Token validation failed: %s", exc)
        raise credentials_exception
 
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user
 
 
async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
