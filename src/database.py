from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# load env
BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
load_dotenv(os.path.join(BASE_DIR, '.env'))


DATABASE_URL = os.getenv("POSTGRES_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
