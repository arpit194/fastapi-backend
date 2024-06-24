from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from api.configs.settings import get_app_settings


settings = get_app_settings()
engine = create_engine(url=settings.DB_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db() -> Session:
    return SessionLocal()
