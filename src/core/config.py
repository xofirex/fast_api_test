import os
from dotenv import load_dotenv

env_path = os.environ['ENV_PATH']
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = 'FastApi Test Task'

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'tdd')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE = 60 * 60 * 24 * 7  # seconds * minutes * hours * days

    TEST_USER_EMAIL = 'test@example.com'

    ORIGINS: list = ['*']


settings = Settings()
