from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHECMY_DATABASE_URL = 'sqlite:///mydatabase.db'

engine = create_engine(SQLALCHECMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


