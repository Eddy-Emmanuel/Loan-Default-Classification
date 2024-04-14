import sys
sys.path.append("./")

from config.configuration import BACKEND_CONFIG

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(url=BACKEND_CONFIG().URL, connect_args={"check_same_thread":False})
Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()