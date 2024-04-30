from sqlalchemy import String
from sqlalchemy.orm import relationship, backref, mapped_column, Mapped

from app.database import Base
from .maps.follow import follow_table
from .maps.wish import wish_table

from datetime import datetime

from app.models.notification import Notification
from app.models.card import Card
from app.models.wish import Wish

# User model
class User(Base):
	# Name of the table
	__tablename__ = "users"

	#columns
	username: Mapped[str] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(nullable=False)
	hashed_password: Mapped[str] = mapped_column(nullable=False)
	email: Mapped[str] = mapped_column(nullable=True)
	gender: Mapped[str] = mapped_column(nullable=True)
	birthday: Mapped[datetime] = mapped_column()
	profile_pic: Mapped[str | None] = mapped_column(nullable=True)

	# Relationships
	notifications = relationship("Notification",cascade="all, delete")
	
	# Represent all the followers
	follows = relationship(
		"User",
		secondary=follow_table, 
		primaryjoin=(username == follow_table.c.username),
		secondaryjoin=(username == follow_table.c.following_username),
		backref=backref("followers", lazy="dynamic"),
		lazy="dynamic"
	)

	

	# Represent all the cards
	cards = relationship("Card")

	
