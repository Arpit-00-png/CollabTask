from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User
if TYPE_CHECKING : 
    from app.models.task import Task


class Comment (SQLModel , table = True):
    id : int = Field(primary_key=True, index= True)
    text : str = Field (nullable = False)
    created_at : datetime = Field( default_factory= datetime.utcnow)
    user_id : int = Field(foreign_key="users.id")
    task_id : int = Field(foreign_key="task.id")

    task: Optional["Task"]= Relationship(back_populates="comments")
    user: Optional["User"]= Relationship(back_populates="comments")