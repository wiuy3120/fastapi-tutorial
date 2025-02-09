import os
import sys
from re import S

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

# this is to include backend dir in sys.path
# so that we can import from db,main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apis.base import api_router  # noqa
from db.base_class import Base  # noqa
from db.session import get_db  # noqa


def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
# Use connect_args parameter only with sqlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def app():
    """
    Create a fresh database for each test case.

    This fixture creates all database tables
    before yielding the application instance
    and drops all tables after the tests are done.
    """
    Base.metadata.create_all(bind=engine)
    _app = start_application()
    yield _app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI):
    """
    Dependency to get a fresh database session for each test case.
    """
    with engine.connect() as connection:
        transaction = connection.begin()
        with SessionTesting(bind=connection) as session:
            yield session
        transaction.rollback()


@pytest.fixture(scope="function")
def client(app: FastAPI, db_session: Session):
    """
    Create a TestClient instance for making requests to FastAPI app.

    This fixture overrides `get_db` dependency, that is injected into routes,
    to use a test database session (`db_session` fixture).
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as test_client:
        yield test_client
