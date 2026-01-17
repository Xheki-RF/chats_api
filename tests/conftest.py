import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from app.db.db import get_session
from sqlalchemy.pool import StaticPool
import app.db.db as db_module
from main import app


# Use a temporary in-memory database for tests
TEST_DATABASE_URL = "sqlite:///:memory:"
ram_engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
db_module.engine = ram_engine


# Override FastAPI's dependency
def override_get_session():
    with Session(ram_engine) as session:
        yield session


app.dependency_overrides[get_session] = override_get_session


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(ram_engine)
    yield
    SQLModel.metadata.drop_all(ram_engine)


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def create_chat():
    def _create_chat():
        chat = {"title": "House chat"}
        
        return chat

    return _create_chat


@pytest.fixture(scope="function")
def create_message():
    def _create_message(single=True):
        if single:
            message = {"text": "Hello everyone!"}
        else:
            message = [
                {"text": "Hello guys!"},
                    {"text": "How are you?"},
                    {"text": "I am good, thanks. And you?"},
                    {"text": "I am fine, thanks for asking!"},
            ]

        return message

    return _create_message

