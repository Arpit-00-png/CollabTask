from passlib.context import CryptContext
from datetime import datetime , timedelta 
from app.core.config import settings 
import jwt

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password : str):
    hashed_password= pwd_context.hash(password)
    return hashed_password

def verify_password(original_password : str,  hashed_password: str):
    return pwd_context.verify(original_password,hashed_password)

def create_access_token(data : dict):
    to_encode=data.copy()
    expire = datetime.utcnow() + timedelta(minutes = settings.TOKEN_EXPIRE_TIME)
    to_encode.update({"exp":expire})
    token= jwt.encode(to_encode,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM)

    return token