import logging
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlalchemy.orm import Session
 
from src.core.database import get_db
from src.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from src.models.user import User
from src.schemas.user import UserCreate, UserRead, Token
 
logger = logging.getLogger(__name__)
limiter = Limiter(key_func=get_remote_address)
router = APIRouter(prefix="/auth", tags=["auth"])
 
 
@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
@limiter.limit("10/minute")
def register(request: Request, user_in: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        full_name=user_in.full_name,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info("New user registered: %s", user.email)
    return user
 
 
@router.post("/login", response_model=Token)
@limiter.limit("5/minute")
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        logger.warning("Failed login attempt for: %s", form_data.username)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    logger.info("User logged in: %s", user.email)
    return {
        "access_token": create_access_token(subject=user.email),
        "refresh_token": create_refresh_token(subject=user.email),
        "token_type": "bearer",
    }
