import logging
import logging.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from core.configs.base import get_env
from core.middlewares.logging_middleware import LoggingMiddleware

db = SQLAlchemy()


class App(Flask):
    """Create Flask App"""

    def __init__(self, name: str):
        super().__init__(name)
        self.set_environment()
        self.set_blueprint()
        self.db_init()
        self.set_logger()
        self.add_middleware()

    def set_environment(self):
        env = get_env()
        self.config.from_object(f'core.configs.{env}')
        self.env = env

    def set_blueprint(self):
        from app_status.controllers import main
        self.register_blueprint(main)

    def db_init(self):
        db.init_app(self)

    def set_logger(self):
        logging_config = self.config['LOGGING']
        logging.config.dictConfig(logging_config)
        _logger = logging.getLogger('werkzeug')
        _logger.disabled = True

    def add_middleware(self):
        self.wsgi_app = LoggingMiddleware(self.wsgi_app)


def run_flask_app(name):
    app = App(name)
    app.run()
