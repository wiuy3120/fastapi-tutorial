from fastapi import FastAPI

from apis.base import api_router
from core.config import settings
from db import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app: FastAPI):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
