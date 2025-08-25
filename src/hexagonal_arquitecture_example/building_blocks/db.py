from sqlmodel import SQLModel, create_engine, Session
from hexagonal_arquitecture_example.infrastructure.models.order_model import OrderModel
from dotenv import load_dotenv
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session_database():
    with Session(engine) as session:
        yield session
