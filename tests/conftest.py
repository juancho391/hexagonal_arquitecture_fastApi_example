import pytest
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()


# Test database setup
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
test_engine = create_engine(TEST_DATABASE_URL)


@pytest.fixture(autouse=True)
def clean_up_database():
    SQLModel.metadata.drop_all(test_engine)
    SQLModel.metadata.create_all(test_engine)
    yield


def get_session_test_db():
    with Session(test_engine) as session:
        yield session
