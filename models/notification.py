from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP, MetaData
from sqlalchemy.orm import relationship

from app.database import Base

# TODO: Implement way to find notifications are closed 
class Notification(Base):
	# Name of the table
	__tablename__ = "notification"

	#columns
	username = Column(String, ForeignKey("user.username"), primary_key=True)
	timestamp = Column(TIMESTAMP)
	content = Column(String, nullable=False, primary_key=True)

	user = relationship("User", back_populates="user")