from sqlalchemy import ForeignKey, func, TIMESTAMP
from sqlalchemy.orm import relationship, mapped_column, Mapped

from app.database import Base

from datetime import datetime


# TODO: Implement way to find notifications are closed 
class Notification(Base):
	# Name of the table
	__tablename__ = "notification"

	#columns
	username: Mapped[str] = mapped_column(ForeignKey("users.username"), primary_key=True)
	timestamp: Mapped[datetime] = mapped_column(TIMESTAMP)
	content: Mapped[str] = mapped_column(nullable=False, primary_key=True)