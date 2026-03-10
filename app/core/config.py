from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY : str
    JWT_ALGORITHM: str
    TOKEN_EXPIRE_TIME : int
    class Config:
        env_file=".env"

settings= Settings()