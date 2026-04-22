import logging
import logging.config
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
 
from src.api.v1.routers.auth.router import router as auth_router
from src.core.security.dependencies import get_current_active_user
from src.models.user import User
from src.schemas.user import UserRead
from src.core.config.settings import get_settings
from src.core.exceptions import EnterpriseAPIException, enterprise_exception_handler
 
settings = get_settings()
 
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"default": {"format": "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "default"}},
    "root": {"level": "INFO", "handlers": ["console"]},
})
 
limiter = Limiter(key_func=get_remote_address)
 
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Enterprise-grade FastAPI backend",
    version=settings.VERSION,
)
 
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(EnterpriseAPIException, enterprise_exception_handler)
app.include_router(auth_router)
 
 
@app.get("/users/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
 
 
@app.get("/health")
async def health_check():
    return {"status": "operational", "version": settings.VERSION}
