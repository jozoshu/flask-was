import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'), verbose=True)

DEFAULT_TIMEZONE = 'Asia/Seoul'


def get_env() -> str:
    env = os.environ.get('ENV')
    if not env:
        raise ValueError('Set ENV variable in `.env` file')

    if env not in ('local', 'development', 'production'):
        raise ValueError('ENV variable choices are local, development and production')

    return env


class Config:
    @staticmethod
    def set_config_common(app):
        config = {
            'BASE_DIR': BASE_DIR,
            'SECRET_KEY': os.environ.get('SECRET_KEY'),
            'SQLALCHEMY_DATABASE_URI': os.environ.get('SQLALCHEMY_DATABASE_URI'),
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        }
        app.config |= config

    @staticmethod
    def set_config_development(app, env):
        app.env = env
        app.debug = True
        app.config['SERVER_NAME'] = 'localhost:8080'

    @staticmethod
    def set_config_production(app, env):
        app.env = env
        app.debug = False
        app.config['SERVER_NAME'] = '0.0.0.0:80'


config_map = {
    'common': Config.set_config_common,
    'local': Config.set_config_development,
    'development': Config.set_config_development,
    'production': Config.set_config_production,
}
