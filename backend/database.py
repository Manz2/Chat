from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Datenbank-URL für SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./chat.db"

# Für SQLite: connect_args nötig für Multithreading
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session-Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base für Models
Base = declarative_base()

# Dependency für FastAPI-Routen
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
