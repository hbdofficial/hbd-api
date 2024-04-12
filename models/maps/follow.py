from sqlalchemy import Table , Column, String, ForeignKey, DateTime
from app.database import Base

# Mapping table to map 2 users 
follow_table = Table(
	"friends",
	Base.metadata,
	Column("username",String, ForeignKey("users.username"), primary_key=True),
	Column("following_username",String, ForeignKey("users.username") ,primary_key=True),
	Column("date_followed",DateTime)
)