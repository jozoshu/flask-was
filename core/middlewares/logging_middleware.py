import uuid

import logging

logger = logging.getLogger('flask.request')


class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        key = str(uuid.uuid4())[-12:]
        method = environ.get('REQUEST_METHOD')
        uri = environ.get('REQUEST_URI')

        logger.info(f'[{key}] - {method} {uri}')

        def _start_response(status, headers, *args):
            logger.info(f'[{key}] - {method} {uri} - {status}')
            return start_response(status, headers, *args)

        return self.app(environ, _start_response)
