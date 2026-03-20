from pydantic import BaseModel
from datetime import datetime
from app.schemas.user import UserResponse

class CommentCreate (BaseModel):
    text : str

class CommentResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    user_id: int
    user: UserResponse  

    class Config:
        from_attributes = True