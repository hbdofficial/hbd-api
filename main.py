from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

# Model used to represent card info
class Card(BaseModel):
	card_no: str
	holder_name: str
	expiry_date: date


# Model used to represent user model
class User(BaseModel):
	username: str
	name: str
	birthday: date # Will be converted to necessary date object
	gender: str
	email: str
	profile_pic: str | None = None
	friends: list[User]

app = FastAPI()

@app.get("/users/{username}")
def user_data(username: str):
	pass