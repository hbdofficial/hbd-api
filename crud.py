# This file contains all the functions related to CRUD operations
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User

def get_user(db: Session, username: str):
	query = select(User).where(User.username == username)
	print(query)
	return db.scalars(query).first()