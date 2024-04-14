import sys
sys.path.append("./")

from database.session import Base

from sqlalchemy import Column, Integer, String

class TABLE(Base):
    __tablename__ = "USER_DATABASE"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)