from pydantic import BaseModel 
from app.models.activity import Description
from typing import Optional
from app.schemas.user import UserResponse
from datetime import datetime


class ActivityResponse(BaseModel):
    id: int
    action_type: Description
    description: Optional[str]
    created_at: datetime 
    user:UserResponse

    class Config:
        from_attributes=True
