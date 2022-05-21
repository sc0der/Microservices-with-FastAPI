from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_USER = env.get('POSTGRES_USER')
    DB_PASSWORD = env.get('POSTGRES_PASSWORD')
    DB_DB = env.get('POSTGRES_DB')
    DB_HOST = env.get('POSTGRES_HOST')
    DB_PORT = env.get('POSTGRES_PORT')

settings = Settings()