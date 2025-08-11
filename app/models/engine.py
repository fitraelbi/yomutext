from sqlmodel import create_engine, Session
from app.core.settings import settings


engine =create_engine(settings.DATABASE_URL)

def db_session():
    with Session(engine) as session:
        yield session