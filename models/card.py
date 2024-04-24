from sqlalchemy import ForeignKey
from app.database import Base 	
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

# Model for storing credit cards
class Card(Base):
	__tablename__ = "card"

	card_no: Mapped[str] = mapped_column(primary_key=True)
	username: Mapped[str] = mapped_column(ForeignKey("users.username") ,primary_key=True)
	holder_name: Mapped[str] = mapped_column(nullable=False)
	expiry_date: Mapped[datetime] = mapped_column(nullable=False)
	