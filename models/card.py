from sqlalchemy import Column, String, DateTime, ForeignKey
from app.database import Base 	

# Model for storing credit cards
class Card(Base):
	__tablename__ = "card"

	card_no = Column(String,primary_key=True)
	username = Column(String, ForeignKey("user.username") ,primary_key=True)
	holder_name = Column(String, nullable=False)
	expiry_date = Column(DateTime, nullable=False)
	