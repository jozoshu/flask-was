from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from core.config import get_env, config_map

db = SQLAlchemy()


class App(Flask):
    """Create Flask App"""

    def __init__(self, name: str):
        super().__init__(name)
        self.set_environment()
        self.set_blueprint()
        self.db_init()

    def set_environment(self):
        config_map['common'](self)

        env = get_env()
        func = config_map[env]
        func(self, env)

    def set_blueprint(self):
        from app_status.controllers import main
        self.register_blueprint(main)

    def db_init(self):
        db.init_app(self)


def run_flask_app(name):
    app = App(name)
    app.run()
