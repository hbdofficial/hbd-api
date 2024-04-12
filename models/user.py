from sqlalchemy import Column,String, Date, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from app.database import Base
from .maps.follow import follow_table

# User model
class User(Base):
	# Name of the table
	__tablename__ = "users"

	#columns
	username = Column(String, primary_key=True)
	name = Column(String, nullable=False)
	hashed_password = Column(String, nullable=False)
	email = Column(String, nullable=True)
	gender = Column(String, nullable=True)
	birthday = Column(Date)
	profile_pic = Column(String, nullable=True)

	# Relationships
	notifications = relationship("Notification", back_populates="users", cascade="all, delete")
	follows = relationship(
		"User",
		secondary=follow_table, 
		primaryjoin=(username == follow_table.c.username),
		secondaryjoin=(username == follow_table.c.following_username),
		backref=backref("followers", lazy="dynamic"),
		lazy="dynamic"
	)
	cards = relationship("Card", back_populates="users")