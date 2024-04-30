import tempfile
import os
import shutil
# This file contains all the functions related to CRUD operations
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from app.models.user import User
from app.models.wish import Wish

from schemas import UnsafeUser
from firebase import bucket

# This function will return a Pydantic model corresponding to the return object
def get_user(db: Session, username: str) -> UnsafeUser:
	""" Retrieving a single user object """
	query = select(User).where(User.username == username)
	# Returing the first user object
	return db.scalars(query).first()

def get_users_birthdays(db: Session, day: int, month: int):
	query = (select(User.birthday, User.username, User.wishes_received)
		.where(func.extract("month", User.birthday) == month)
		.where(func.extract("day", User.birthday) == day)
	)
	
	return db.execute(query).all()


def set_wish(id: str,wishes_by: str, wishes_to: str, db: Session):
	new_wish = Wish(
		story_id = id,
		wishes_to=wishes_to,
		wishes_by=wishes_by
	)
	db.add(new_wish)
	db.commit()

def is_user_available(db: Session, username: str) -> bool:
	"""Retrieving whether a user is awailable"""
	query = select(User.username).where(User.username == username)

	result = db.scalars(query).first()

	if result:
		return True
	else:
		return False

def download(bucket_path):
	blob = bucket.blob(bucket_path)
	temp_file_name = ""

	# Blob is not awailable
	if blob is None:
		return False

	try:
		# Making a temporary file to store the image
		_, temp_file_name = tempfile.mkstemp(suffix=".jpg")
	except Exception as e:
		raise Exception(f"Error while making the temp file or copying from the tempfile (detail: {e})")

	try:
		blob.download_to_filename(temp_file_name)
	except Exception as e:
		raise Exception(f"Error while downloading from firebase storage bucket (detail: {e})")

	def file_iterator():
		""" Function used to send the image """
		with open(temp_file_name, mode="rb") as file_like:
			yield from file_like
			removed = False
			# Giving multiple tries to delete
			for i in range(10):
				try: 
					if not removed:	
						os.remove(temp_file_name)
						removed = True
						break
				except:
					pass
			print(removed)

	
	return file_iterator

def upload(file, file_type, upload_path):
	blob = bucket.blob(upload_path)

	# FROM GOOGLE CLOUD DOCS
	# Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
	
	#generation_match_precondition = 1

	temp_file_name = ""

	try:
		# Making a temporary file
		_, temp_file_name = tempfile.mkstemp(suffix=file_type)

		# Writing to temporary file
		with open(temp_file_name, "wb") as temp_image:
			shutil.copyfileobj(file, temp_image)
	except Exception as e:
		raise Exception(f"Error while making or copying to the tempfile (detail: {e})")

	try:
		blob.upload_from_filename(
			temp_file_name, 
		)

		# To save space the tempfiles are deleted
		removed = False
			# Giving multiple tries to delete
		for i in range(10):
			try: 
				if not removed:	
					os.remove(temp_file_name)
					removed = True
					break
			except:
				pass
		print(removed)
		
	except Exception as e:
		raise Exception(f"Error while downloading from firebase storage bucket (detail: {e})")