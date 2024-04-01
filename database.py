from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string 
SQL_ALCHEMY_DATABASE_URL = "postgresql://postgres:rasuwank@localhost:5432/hbd"

engine = create_engine(
	SQL_ALCHEMY_DATABASE_URL,
	connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()