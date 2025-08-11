from sqlmodel import Session, select
from typing import Sequence

from app.models.users import User
from app.schema.user import UserCreate, UserUpdate


def create_user(db_session: Session, user: UserCreate) -> User:
    db_user = User(**user.model_dump())

    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)

    return db_user


def get_user(db_session: Session, user_id: str) -> User | None:
    return db_session.get(User, user_id)


def get_users(db_session: Session) -> Sequence[User]:
    return db_session.exec(select(User)).all()


def update_user(db_session: Session, user_id: str, user: UserUpdate) -> User | None:
    db_user = db_session.get(User, user_id)

    if not db_user:
        return None

    user_data = user.model_dump(exclude_unset=True)

    for key, value in user_data.items():
        setattr(db_user, key, value)
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)

    return db_user


def delete_user(db_session: Session, user_id: str) -> dict | None:
    db_user = get_user(db_session, user_id)

    if not db_user:
        return None

    db_session.delete(db_user)
    db_session.commit()

    return {"ok": True}
