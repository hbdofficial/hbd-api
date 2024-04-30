import uuid
from sqlalchemy import Table , Column, String, ForeignKey, DateTime
from app.database import Base

# Mapping table to map the wishes
wish_table = Table(
	"wishes_table",
	Base.metadata,
	Column("story_id",String, primary_key=True),
	Column("wishes_to",String, ForeignKey("users.username")),
	Column("wished_by",String, ForeignKey("users.username")),
	Column("wished_time", DateTime)
)