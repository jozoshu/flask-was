from .base import *


SERVER_NAME = 'localhost:8080'

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] - %(name)s - [%(levelname)s] - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'default',
        },
        'file.info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'default',
            'filename': f'{BASE_DIR}/logs/info.log',
        }
    },
    'loggers': {
        'flask.request': {
            'handlers': ['console', 'file.info'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
