from sqlalchemy.orm import Session

from db.repository.user import create_new_user
from schemas.user import CreateUser


def create_random_user(db: Session):
    email = "random_user@nofoobar.com"
    password = "random_password"
    return create_new_user(CreateUser(email=email, password=password), db)
