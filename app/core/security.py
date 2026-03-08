from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password : str):
    hashed_password= pwd_context.hash(password)
    return hashed_password

def verify_password(hashed_password : str, original_password : str):
    return pwd_context.verify(hashed_password, original_password)