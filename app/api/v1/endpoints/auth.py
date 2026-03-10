from fastapi import APIRouter,HTTPException, Depends
from app.schemas.user import UserResponse, UserCreate, UserLogin
from app.db.sessions import getdb
from app.models.user import User
from sqlmodel import Session, select
from app.core.security import hash_password, verify_password, create_access_token
from app.core.oauth2 import get_current_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router=APIRouter()

@router.get("/testrouter")
def testrouter():
    return {"message":"this router came from another file"}

@router.post("/register",response_model=UserResponse)
def register_user( user : UserCreate, db: Session=Depends(getdb)):
    if not user:
        raise HTTPException(status_code = 404, detail= "input not found")
    user.password=hash_password(user.password)
    item= User(**user.model_dump())
    if not item :
        raise HTTPException(status_code = 404, detail= "input not found")

    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.post("/login")
def login_user(user : OAuth2PasswordRequestForm= Depends(), db: Session=Depends(getdb)):
    statement =select(User).where(User.email==user.username)
    item =db.exec(statement).first()
    if not item:
        raise HTTPException(status_code=404, detail="user not found in the database")
    if not verify_password(user.password,item.password):
        raise HTTPException(status_code=405, detail="the provided password is wrong")
    data={}
    data.update({"sub":user.username})
    token= create_access_token(data)

    return {
        "access_token":token,
        "token_type":"bearer"
    }

@router.get("/me",response_model=UserResponse)
def get_user_info(user : User = Depends(get_current_user)):
    if not user :
        raise HTTPException(status_code=404, detail="user not found")

    return user