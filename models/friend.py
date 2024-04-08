from sqlalchemy import ForeignKey, Column, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Follow(Base):
	__tablename__ = "friend"

	username = Column(String, ForeignKey("user.username"), primary_key=True)
	follow_username = Column(String, ForeignKey("user.username") ,primary_key=True)
	follow_date = Column(DateTime)

	#users = relationship("User", back_populates="users")