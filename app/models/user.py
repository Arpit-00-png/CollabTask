from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import EmailStr


class User ( SQLModel, table=True):
    __tablename__="users"

    id: int = Field(primary_key=True, index=True)
    email : EmailStr = Field(nullable=False, unique = True)
    username : str= Field(nullable=False)
    password: str= Field(nullable=False)
    isactive: bool = Field(default= True)
    created_at: datetime = Field(default= datetime.utcnow())