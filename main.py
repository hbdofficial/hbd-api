import uuid
from fastapi import FastAPI, Depends, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from sqlalchemy.orm import Session

app = FastAPI()

# This file contains everything related to the user route

from crud import get_user, download, is_user_available, upload, get_users_birthdays, set_wish
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
def profile_pic_get(username: str, db: Session = Depends(get_db)):
	# TODO: Add a authentication, temp file removal
	# TODO: Add proper exceptions
	# TODO: Image format must be discussed and selected (.jpeg won't be a thing)

	if is_user_available(db, username):
		try:
			file_iterator = download(f"{username}/profile_pics/img.jpg")
			content_type = "image/jpg"
			return StreamingResponse(file_iterator(), media_type=content_type)
		except Exception as e:
			return HTTPException(status_code=500, detail=f"Error occured retrieving the profile pic (Error:{e})")
	else:
		return HTTPException(status_code=404, detail="User not found")

@app.post("/users/{username}/profile_pic")
async def profile_pic_post(image_file_input: UploadFile, username: str,db: Session = Depends(get_db)):
	if is_user_available(db, username):
		# Taking upload file information
		image_filename = image_file_input.filename 
		image_file = image_file_input.file
		image_file_type = ""

		# checking the file type, only jpg, jpeg and png are accepted, heic, heif
		if image_filename.endswith(".jpg"):
			image_file_type = "jpg"
		elif image_filename.endswith(".jpeg"):
			image_file_type = "jpeg"
		elif image_filename.endswith(".png"):
			image_file_type = "png"
		elif image_filename.endswith(".heic"):
			image_file_type = "heic"
		elif image_filename.endswith(".heif"):
			image_filename = "heif"
		else:
			return HTTPException(status_code=404, detail="Invalid file format, must be jpg, jpeg, png, heic, heif")

		# TODO: Add a profile pic size checker
		try:
			upload(image_file, image_file_type, f"{username}/profile_pics/img.{image_file_type}")
			return {"success": True, "message": "Profile pic uploaded successfully"}
		except Exception as e:
			return HTTPException(status_code=500, detail=f"Error while processing the file, error: {str(e)}")

	else:
		return HTTPException(status_code=404, detail="User not found")

@app.get("/birthdays")
def birthdays_route(month: int, day: int, db: Session = Depends(get_db)):
	# Get all the posted stories of the person who has birthdays today
	# If no one has wished on the birthday no stories will be empty
	users_with_birthdays = get_users_birthdays(db, day, month)

	
	return "Success"
	
@app.post("/users/{username}/wish/")
def wish_route(username: str,by: str, story_file_input: UploadFile, db: Session = Depends(get_db)):
	if is_user_available(db, username):
		# Taking upload file information
		story_filename = story_file_input.filename 
		story_file = story_file_input.file
		story_file_type = ""

		# Using a uuid for a filename
		story_id = uuid.uuid4()

		# checking the file type, only jpg, jpeg and png are accepted, heic, heif
		if story_filename.endswith(".jpg"):
			story_file_type = "jpg"
		elif story_filename.endswith(".jpeg"):
			story_file_type = "jpeg"
		elif story_filename.endswith(".png"):
			story_file_type = "png"
		elif story_filename.endswith(".heic"):
			story_file_type = "heic"
		elif story_filename.endswith(".heif"):
			story_filename = "heif"
		elif story_filename.endswith(".hevc"):
			story_file_type = "hevc"
		elif story_filename.endswith(".mp4"):
			story_file_type = "mp4"
		else:
			return HTTPException(status_code=404, detail="Invalid file format, must be jpg, jpeg, png, heic, heif")

		# TODO: A bug is located here
		try:
			pass
			#set_wish(story_id, by, username)
		except Exception as e:
			return HTTPException(status_code=500, detail=f"Database error (detail: {e})")

		try:
			upload(story_file, story_file_type, f"{username}/stories/{story_id}.{story_file_type}")
		except Exception as e:
			return HTTPException(status_code=500, detail=f"Error while processing the file, error: {str(e)}")

	else:
		return HTTPException(status_code=404, detail="User not found")

@app.get("/")
async def test_route():
	content = """
		<html>
			<head>
				<title>Upload image</title>
			</head>
			<form action="/users/kay/profile_pic" method="post" enctype="multipart/form-data">
				<label>Enter the file: <input type="file" name="image_file_input"/></label>
				<button type="submit">Submit file</button>
			</form>
		</html>
	"""

	return HTMLResponse(content=content)
	