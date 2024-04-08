# This file contains everything related to the user route

from app.main import app 


@app.get("/users/{username}")
def route(username: str):
	pass