from fastapi import FastAPI, Depends
from src.api.v1.auth.router import router as auth_router
from src.core.security.dependencies import get_current_active_user
from src.models.user import User
from src.schemas.user import UserRead
from src.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Enterprise-grade FastAPI backend",
    version="0.1.0",
)

# Include routers
app.include_router(auth_router)


# Example protected route
@app.get("/users/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
