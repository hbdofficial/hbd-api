from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint

from .database import Base

class User(Base):
	# Name of the table
	__tablename__ = "user"

	#columns
	username = Column(String, primary_key=True)
	name = Column(String, nullable=False)
	hashed_password = Column(String, nullable=False)
	email = Column(String, nullable=True)
	gender = Column(String, nullable=True)
	birthday = Column(Date)
	profile_pic = Column(String, nullable=True)

	# Relationships
	#notifications = relationship("Notification", back_populates="notification")

# TODO: Implement way to find notifications are closed 
class Notification(Base):
	# Name of the table
	__tablename__ = "notification"

	#columns
	username = Column(String, ForeignKey("user"), primary_key=True)
	timestamp = Column(TIMESTAMP, primary_key=True)
	content = Column(String, nullable=False)

	user = relationship("User", back_populates="user")

	# Used to add composite key constraints
	__table_args__ = (
		PrimaryKeyConstraint("username","timestamp"),
	)