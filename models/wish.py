from datetime import datetime
from database import Base
from sqlalchemy import Column , String , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Wish(Base):
    __tablename__ = "wishes"

    story_id: Mapped[str] = mapped_column(primary_key=True)
    wishes_to: Mapped[str] = mapped_column(ForeignKey("users.username"))
    wished_by: Mapped[str] = mapped_column(ForeignKey("users.username"))
    wished_time: Mapped[datetime] = mapped_column(nullable=True)