import logging

logger = logging.getLogger('flask.request')


class JWTMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        token = environ.get('HTTP_AUTHORIZATION')

        return self.app(environ, start_response)
