from sqlalchemy.orm import sessionmaker, declarative_base
from app.database.connection import SessionLocal


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()