from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import Config

def get_session():
    engine = create_engine(
        Config.SQLALCHEMY_DATABASE_URI,
        **Config.SQLALCHEMY_ENGINE_OPTIONS
    )
    return sessionmaker(bind=engine)()
