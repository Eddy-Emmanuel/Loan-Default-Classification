from os import getenv
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(".env")

class BACKEND_CONFIG(BaseSettings):
    URL : str = getenv("DATABASE_URL")
    SECRET : str = getenv("SECRET")
    ALGORITHM : str = getenv("ALGORITHM")