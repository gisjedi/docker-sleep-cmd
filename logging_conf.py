CONFIG = {
            'version': 1,
            'formatters': {
                'detailed': {
                    'class': 'logging.Formatter',
                    'format': '%(asctime)s %(name)-15s %(levelname)-8s %(message)s'
                }
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'detailed'
                }
            },
            'loggers': {
                '': {
                    'handlers': ['console']
                }
            },
            'root': {
                'level': 'DEBUG',
                'handlers': ['console']
            },
        }
