from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

# This file contains everything related to the user route

from crud import get_user
from database import SessionLocal

from app.schemas import SafeUser, UnsafeUser

# Function to open a database session for each request and 
# close when the request finishes

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.get("/users/{username}", response_model=UnsafeUser)
def route(username: str,  db: Session = Depends(get_db)):
	# TODO: Return friends
	# Get the result from the orm
	user = get_user(db,username)
	
	if user:
		print(user.cards)
		return user
	else:
		# In case such user is not in the database
		return HTTPException(404, "User not found")
