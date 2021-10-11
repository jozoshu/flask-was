from datetime import timedelta
import os

from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'), verbose=True)


def get_env() -> str:
    env = os.environ.get('ENV')
    if not env:
        raise ValueError('Set ENV variable in `.env` file')

    if env not in ('local', 'development', 'production'):
        raise ValueError('ENV variable choices are local, development and production')

    return env


SECRET_KEY = os.environ.get('SECRET_KEY')

DEFAULT_TIMEZONE = 'Asia/Seoul'

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_EXPIRED_INTERVAL = timedelta(hours=24)
