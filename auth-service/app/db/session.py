from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
print(settings.SQLALCHEMY_DATABASE_URL)
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)