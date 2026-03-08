from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import auth

print(settings.ALGORITHM)

def create_application():
    app= FastAPI()
    return app


app=create_application()

app.include_router(auth.router)
@app.get("/")
def intro():
    return f"hello world + {settings.ALGORITHM}"