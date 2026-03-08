from sqlmodel import Session, create_engine
from app.core.config import settings


engine= create_engine(settings.DATABASE_URL)


def getdb():
    try :
        db=Session(engine)
        yield db
    finally :db.close()