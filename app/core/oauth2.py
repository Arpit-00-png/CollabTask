from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError, ExpiredSignatureError
from sqlmodel import Session, select
from app.db.sessions import getdb
from fastapi import HTTPException, Depends
from app.core.config import settings
from app.models.user import User
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def verify_token(token : str, db: Session):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    email=payload.get("sub")

    if not email:
        raise HTTPException(status_code=401 , detail="token verification failed")

    statement=select(User).where(User.email==email)
    item=db.exec(statement).first()
    if not item:
        raise HTTPException(status_code=401 , detail="an error occured")

    return item



def get_current_user(token : str = Depends(oauth2_scheme), db : Session= Depends(getdb)):
    return verify_token(token,db)