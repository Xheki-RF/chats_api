from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv


load_dotenv()

engine = None

def get_engine():
    global engine

    if engine is not None:
        return engine
    
    DB_URL = os.getenv("DB_URL")

    if not DB_URL:
        raise ValueError("DB_URL environment variable is not set!")

    engine = create_engine(DB_URL, echo=False)

    return engine


def init_db():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
