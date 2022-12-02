from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Configuration(BaseSettings):
    env: str = "dev"
    db_url: str = "sqlite:///./fastapi_shortener/src/db/shortener.db"
    # We can keep adding other configurations here
    
def load_db(settings):
    engine = create_engine(
        settings.db_url, connect_args={"check_same_thread": False}
    )
    SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    Base = declarative_base()
    return engine, Base, SessionLocal


settings = Configuration()
print(f"Environment: {settings.env}")

engine, base, session_local = load_db(settings)
