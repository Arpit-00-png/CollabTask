from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password:str

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    isactive: bool
    class Config:
        from_attributes=True   # To be able to handle the Objects that come in response from the Database instead of Dictionaries

class UserLogin(BaseModel):
    email:EmailStr
    password: str
