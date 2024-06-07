"""Configs for script."""
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API_KEY')
secret_key = os.getenv('API_NAME')

class Config:
    """DB connections."""

    DB_USER = os.getenv("DB_USERNAME")
    DB_PASSWD = os.getenv("DB_PASSWD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


config = Config()