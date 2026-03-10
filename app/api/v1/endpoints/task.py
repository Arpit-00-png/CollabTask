from fastapi import APIRouter, HTTPException, Depends, Query
from app.schemas.task import TaskResponse, TaskCreate, TaskUpdate, TaskListResponse
from app.db.sessions import getdb
from app.models.task import Task
from app.core.oauth2 import get_current_user
from app.models.user import User
from sqlmodel import Session, select, func
from typing import List
from datetime import datetime

router=APIRouter()

@router.post("/",response_model=TaskResponse)
def posttasks(task: TaskCreate, db: Session= Depends(getdb), user : User = Depends(get_current_user)):
    if not user :
        raise HTTPException(status_code=404, detail="user not found")
    item=Task(**task.model_dump(),owner_id=user.id)

    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/",response_model=TaskListResponse)
def getalltask(page : int =1 , limit: int = Query(10, le=100) , db: Session= Depends(getdb), user : User = Depends(get_current_user)):
    offset = (page - 1) * limit
    count_statement = select(func.count(Task.id)).where(Task.owner_id == user.id)
    total = db.exec(count_statement).one()
    statement = select(Task).where(Task.owner_id == user.id).offset(offset).limit(limit)
    tasks = db.exec(statement).all()
    pages = (total + limit - 1) // limit

    return {
        "tasks": tasks,
        "total": total,
        "page": page,
        "limit": limit,
        "pages": pages
    }

@router.get("/{id}", response_model=TaskResponse)
def getspecifictask(id : int , db: Session=Depends(getdb), user : User = Depends(get_current_user)):
    if not user :
        raise HTTPException(status_code=404, detail="user not found")
    if not id:
        raise HTTPException(status_code=401 , detail="Invalid input")

    statement= select(Task).where(Task.id == id )
    item= db.exec(statement).first()
    if item.owner_id != user.id:
        raise HTTPException(status_code=404, detail="no task found")

    if not item:
        raise HTTPException(status_code=404, detail="no task found")

    return item


@router.put("/{id}", response_model=TaskResponse)
def updatetask(id : int ,updatetask: TaskUpdate, db: Session=Depends(getdb), user : User = Depends(get_current_user)):
    statement = select(Task).where(Task.id==id)
    item= db.exec(statement).first()
    if not item :
        raise HTTPException(status_code=404, detail="no task found")
    if item.owner_id != user.id:
        raise HTTPException(status_code=403, detail="updation now allowed")
    update_data = updatetask.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_data)
    item.updated_at = datetime.utcnow()
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{id}")
def deletetask(id : int ,db: Session=Depends(getdb), user : User = Depends(get_current_user)):
    statement=select(Task).where(Task.id==id)
    item=db.exec(statement).first()
    if not item :
        raise HTTPException(status_code=404, detail="no task found") 
    if item.owner_id != user.id:
        raise HTTPException(status_code=403, detail="deletion now allowed")
    db.delete(item)
    db.commit()
    return {"response": "task deleted successfully"}
    