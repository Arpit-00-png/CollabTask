from fastapi import APIRouter, HTTPException
from app.schemas.comment import CommentResponse, CommentCreate
from sqlmodel import Session, select
from fastapi import Depends
from app.models.user import User
from app.models.comment import Comment
from app.db.sessions import getdb
from app.core.oauth2 import get_current_user
from app.models.task import Task
from typing import List

router = APIRouter()

@router.post("/tasks/{task_id}/comments", response_model = CommentResponse)
def postcomment(task_id:int ,comment: CommentCreate, db: Session= Depends(getdb) , user: User = Depends(get_current_user)):
    statement= select(Task).where(Task.id == task_id)
    item =db.exec(statement).first()

    if not item:
        raise HTTPException (status_code = 404, detail="the required task not found")

    newcomment= Comment( 
        text=comment.text,
        task_id=task_id,
        user_id= user.id
    )
    db.add(newcomment)
    db.commit()
    db.refresh(newcomment)
    return newcomment

@router.get("/tasks/{task_id}/comments", response_model=List[CommentResponse])
def gettaskcomments(task_id : int , user: User = Depends(get_current_user), db: Session= Depends(getdb)):
    statement=select(Comment).where(Comment.task_id==task_id)
    item=db.exec(statement).all()

    if not item:
        raise HTTPException(status_code = 200, detail="[]")

    return item
    
@router.delete("/tasks/{comment_id}/comments")
def deletecomment(comment_id : int , user: User= Depends(get_current_user), db: Session=Depends(getdb)):
    statement=select(Comment).where(Comment.id==comment_id)
    item=db.exec(statement).first() 
    if not item:
        raise HTTPException(status_code = 200, detail="[]")

    if item.user_id != user.id:
        raise HTTPException(status_code = 403, detail="not authorized to delete this comment")  
    
    db.delete(item)
    db.commit()
    return {"message": "comment deleted successfully"}