from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.user import UserResponse
from typing import Optional, List

class TaskCreate(BaseModel):
    title : str
    description : str | None = None
    status : str | None = None
    priority : str | None = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id : int
    title : str
    description : str | None = None
    status : str | None = None
    priority : str | None = None
    created_at: datetime 
    updated_at: datetime
    owner_id : int | None
    owner: UserResponse=None
    due_date: datetime = None
    is_due : bool =True

    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    title : str | None = None
    description : str | None = None
    status : str | None = None
    priority : str | None = None
    due_date: datetime | None = None


class TaskListResponse(BaseModel):
    tasks: List[TaskResponse]  
    total: int                 
    page: int                   
    limit: int                  
    pages: int             

    class Config:
        from_attributes = True