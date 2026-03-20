from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from pydantic import EmailStr
from typing import Optional, TYPE_CHECKING, List


if TYPE_CHECKING:
    from app.models.user import User
    from app.models.activity import Activity
    from app.models.comment import Comment

class Task(SQLModel, table =True):
    id: int =Field(primary_key=True)
    title : str = Field(nullable=False)
    description: str | None = Field(default = None)
    status : str | None = Field(default = None)
    priority : str | None = Field(default = None)
    created_at : datetime =Field(default_factory= datetime.utcnow)
    updated_at: datetime=Field(default_factory= datetime.utcnow) # agar mai datetime.utcnow() use karta default ka saath to dikkat ye hota ki ye funtion bas ek baar run karta jab class load hoti -> which means even for differnt record inputs the created/updated time would have remained the same 
                                                                   # isiliye hamne ek funtion k refrence pass kardiya to har record creation mai call hojata hai 
    due_date : Optional[datetime]= Field(default = None)
    owner_id: int =Field(foreign_key="users.id")
    owner: Optional["User"] = Relationship(back_populates="tasks")
    comments: Optional[List["Comment"]]=Relationship(back_populates="task")
    activities: Optional[List["Activity"]]= Relationship(back_populates="task")
    @property
    def is_due(self):
        if not self.due_date:
            return False;
        return self.due_date<datetime.utcnow()