from pydantic import BaseModel
from datetime import date, datetime

# Schema representing account data (for unauthenticated users)
class SafeUser(BaseModel):
	username: str
	name: str
	email: str
	birthday: date
	gender: str
	profile_pic: str | None

	class Config:
		orm_mode = True

class UnsafeUser(SafeUser):
	cards: list["Card"] | None
	hashed_password: str
	notifications: list["Notification"] | None
	follows: list["SafeUser"] | None



class Notification(BaseModel):
	username:str
	timestamp:datetime
	content: str

	class Config:
		orm_mode = True

# Model capable of storing card information
class Card(BaseModel):
	card_no: str
	username: str
	holder_name: str
	expiry_date: datetime

	class Config:
		orm_mode = True	