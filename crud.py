# This file contains all the functions related to CRUD operations
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User

from schemas import UnsafeUser
from firebase import storage

# This function will return a Pydantic model corresponding to the return object
def get_user(db: Session, username: str) -> UnsafeUser:
	""" Retrieving a single user object """
	query = select(User).where(User.username == username)
	# Returing the first user object
	return db.scalars(query).first()

def download():
	return storage.child("profile_pics/pic.jpg").get_url("profile_pic.jpg")
	
