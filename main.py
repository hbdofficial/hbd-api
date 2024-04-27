import tempfile
import os
from datetime import datetime

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session

app = FastAPI()

# This file contains everything related to the user route

from crud import get_user, download
from database import SessionLocal

from app.schemas import UnsafeUser

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
	# TODO: Add authentication 
	# TODO: Depending on the type of authorization returning user model will be varied
	# Get the result from the orm
	user = get_user(db,username)
	
	if user:
		return user
	else:
		# In case such user is not in the database
		return HTTPException(404, "User not found")

@app.get("/users/{username}/profile_pic")
def route(username: str, db: Session = Depends(get_db)):
	# TODO: Add a authentication, temp file removal
	# TODO: Add proper exceptions
	# TODO: Image format must be discussed and selected (.jpeg won't be a thing)
	user = get_user(db, username)

	if user:
		try:
			# A temporary file is created to save the image
			_, temp_file_name = tempfile.mkstemp(suffix=".jpg")
			# File name is extracted from the path
			file_name = os.path.basename(temp_file_name)
			
			# Downloading the file from the storage bucket
			download(f"{username}/profile_pics/img.jpg", temp_file_name)

			# In case the profile pic folder doesen't contain an image
			if not (file_name.endswith(".jpg") or file_name.endswith(".jpeg")):
				return HTTPException(status_code=500, detail="File in the storage wasn't an image")

			def file_iterator():
				""" Function used to send the image """
				with open(temp_file_name, mode="rb") as file_like:
					yield from file_like
				removed = False
				for i in range(10):
					try: 
						os.remove(temp_file_name)
						removed = True
						break
					except:
						pass
				print(removed)

			
			content_type = "image/jpg"

			return StreamingResponse(file_iterator(), media_type=content_type)
		except:
			return HTTPException(status_code=500, detail="Error occured retrieving the profile pic")
	else:
		return HTTPException(status_code=404, detail="User not found")

@app.post("/users/{username}/profile_pic")
def route():
	pass

@app.get("/test")
def test_route():
	return download()
	