from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP, MetaData
from sqlalchemy.orm import relationship

from app.database import Base

# User model
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