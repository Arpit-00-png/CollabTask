from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from pydantic import EmailStr
from typing import Optional, TYPE_CHECKING, List
from app.models.task import Task

if TYPE_CHECKING : 
    from app.models.task import Task
    from app.models.activity import Activity
    


class User ( SQLModel, table=True):
    __tablename__="users"

    id: int = Field(primary_key=True, index=True)
    email : EmailStr = Field(nullable=False, unique = True)
    username : str= Field(nullable=False)
    password: str= Field(nullable=False)
    isactive: bool = Field(default= True)
    created_at: datetime = Field(default_factory= datetime.utcnow)
    comments: Optional[List["Comment"]]=Relationship(back_populates="user")
    tasks: Optional[List["Task"]]=Relationship(back_populates="owner")
    activities: Optional[List["Activity"]]= Relationship(back_populates="user")
