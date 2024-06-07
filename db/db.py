"""Initialize DB."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import config
from models.models import Base


SQLALCHEMY_DATABASE_URL = config.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)


# This function is a dependency which will be used
# in main.py or anywhere a db session is needed.
def get_db():
    """DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


session = next(get_db())
