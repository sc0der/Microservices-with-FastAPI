from os import environ as env
from dotenv import load_dotenv

load_dotenv(".route.env")

from fastapi import FastAPI

SECRET_KEY = env.get('SECRET_KEY')
ALGORITHM = env.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 1

class Settings:
    DB_USER = env.get('POSTGRES_USER')
    DB_PASSWORD = env.get('POSTGRES_PASSWORD')
    DB_DB = env.get('POSTGRES_DB')
    DB_HOST = env.get('POSTGRES_HOST')
    DB_PORT = env.get('POSTGRES_PORT')

settings = Settings()
