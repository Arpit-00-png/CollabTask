from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.task import Task
    



class Description(Enum):
    Created = "created"
    Deleted = "deleted"
    Updated = "updated"
    Comment_added = "comment_added"

class Activity(SQLModel, table=True):
    __tablename__="activities"

    id : int = Field(primary_key = True, index= True)
    action_type: Description = Field(nullable = False)
    description: str | None = Field(default = None)
    created_at : datetime = Field(default_factory= datetime.utcnow)

    task_id: int = Field(foreign_key="task.id")
    user_id: int = Field(foreign_key="users.id")

    user: Optional["User"] = Relationship(back_populates="activities")
    task: Optional["Task"] = Relationship(back_populates="activities")