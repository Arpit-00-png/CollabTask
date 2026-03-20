from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import auth,task,comment
from app.models import User, Task, Comment, Activity


def create_application():
    app= FastAPI()
    return app


app=create_application()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(task.router, prefix="/api/vi/taks", tags=["Task"])
app.include_router(comment.router, prefix="/api/v1", tags=["Comments"])
@app.get("/")
def intro():
    return {"message":"hello world"}