from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.models.engine import db_session
from app.services.user_service import get_users, get_user, create_user, update_user, delete_user
from app.schema.user import UserCreate,  UserUpdate, UserRead


users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/", response_model=list[UserRead])
def get_users_api(db: Session = Depends(db_session)):
    return get_users(db)

@users_router.get("/{user_id}", response_model=UserRead)
def get_user_api(user_id: str, db: Session = Depends(db_session)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@users_router.post("/", response_model=UserRead, status_code=201)
def create_user_api(user: UserCreate, db: Session = Depends(db_session)):
    return create_user(db, user)

@users_router.put("/{user_id}", response_model=UserRead)
def update_user_api(user_id: str, user: UserUpdate, db: Session = Depends(db_session)):
    db_user = update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@users_router.delete("/{user_id}", status_code=200)   
def delete_user_api(user_id: str, db: Session = Depends(db_session)):
    result = delete_user(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result


    