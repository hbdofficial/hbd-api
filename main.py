from fastapi import FastAPI

app = FastAPI()

# This file contains everything related to the user route

from pydantic import BaseModel
from datetime import date, datetime

from app.main import app 

# Schema representing account data
class Account(BaseModel):
	name: str
	email: str
	birthday: date
	gender: str

# Schema representing credit card information
class Card(BaseModel):
	card_no: str
	holder_name: str
	expiry_date: date

# Schema representing notification information
class Notification(BaseModel):
	timestamp: datetime
	content: str

# Schema representing user data response
class User(BaseModel):
	account: Account
	age: int
	billing_details: list[Card]
	notifications: list[Notification] | None

@app.get("/users/{username}", response_model=User)
def route(username: str) -> User:
	return User(
		account=Account(
			name="Rasuwan Kalhara", 
			email="kalharaweragala@gmail.com", 
			birthday=date(2024,10,1), 
			gender="male"
		),
		billing_details=[
			Card(
				holder_name="W.D.Y.R.Kalhara",
				expiry_date=date(2027,7,2),
				card_no="122342-34-3455-34"
				)],
			age=21,
			notifications=None
		)