from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.user import User
from schemas.user import CreateUser


def create_new_user(user: CreateUser, db: Session):
    new_user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
