from os import environ as env
from dotenv import load_dotenv
import secrets
from pydantic import BaseSettings 

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    

    def db_config(self):
        DB_USER = env.get('POSTGRES_USER')
        DB_PASSWORD = env.get('POSTGRES_PASSWORD')
        DB_DB = env.get('POSTGRES_DB')
        DB_HOST = env.get('POSTGRES_HOST')
        DB_PORT = env.get('POSTGRES_PORT')
        SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DB}"
        return SQLALCHEMY_DATABASE_URL
    
    @property
    def SQLALCHEMY_DATABASE_URL(self):
        return self.db_config()

    FIRST_SUPERUSER = ''
    FIRST_SUPERUSER_PASSWORD = '' 

    PROJECT_NAME = ''
    BACKEND_CORS_ORIGINS = '*'


    class Config:
        case_sensitive = True

settings = Settings()