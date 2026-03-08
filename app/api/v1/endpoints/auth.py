from fastapi import APIRouter,HTTPException, Depends
from app.schemas.user import UserResponse, UserCreate
from app.db.sessions import getdb
from app.models.user import User
from sqlmodel import Session
from app.core.security import hash_password


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