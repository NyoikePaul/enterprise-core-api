import re
from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
from datetime import datetime
from typing import Optional
 
 
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
 
 
class UserCreate(UserBase):
    password: str
 
    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError("Password must contain at least one special character")
        return v
 
 
class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
 
 
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
