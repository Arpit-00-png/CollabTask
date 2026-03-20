from pydantic_settings import BaseSettings

class Settings(BaseSettings):  # ye kyo use karna direct dotenv k jagah - datatype validation provide karta direct import karne mai dikkat hosakta 
    DATABASE_URL: str
    JWT_SECRET_KEY : str
    JWT_ALGORITHM: str
    TOKEN_EXPIRE_TIME : int
    class Config:
        env_file=".env"

settings= Settings()

'''
har jagah ye sab nhi karna padta :
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

'''