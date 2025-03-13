from sqlalchemy.orm import Session
from app.repositories.user_respository import get_users, create_user
from app.shemas.user import UserCreate

def fetch_all_users(db: Session):
    return get_users(db)

def add_new_user(db: Session, user: UserCreate):
    return create_user(db, user)
