from pydantic import BaseSettings

class Settings(BaseSettings){
    DATABASE_URL: str
    SECRET_KEY : str
    ALGORITHM: str

    class config:
        env_file=".env"
}