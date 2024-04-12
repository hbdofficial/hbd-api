from sqlalchemy import Column, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import relationship

from app.database import Base

# TODO: Implement way to find notifications are closed 
class Notification(Base):
	# Name of the table
	__tablename__ = "notification"

	#columns
	username = Column(String, ForeignKey("users.username"), primary_key=True)
	timestamp = Column(TIMESTAMP)
	content = Column(String, nullable=False, primary_key=True)

	user = relationship("User", back_populates="notifications")