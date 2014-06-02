# Django settings for threeandout project.
from threeandout.settings.common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'threeandoutfantasyfootball@gmail.com'


DATABASES = {
    'default': {'ENGINE': 'django.db.backends.mysql', 
                'NAME': 'threeandout',
                'USER': 'threeandout',
                'PASSWORD': 'Thr33&0ut',
                'HOST': 'threeandout.c0bnvpjdlyf5.us-east-1.rds.amazonaws.com',
                'PORT': 3306 },
    'slave': {'ENGINE': 'django.db.backends.sqlite3',
                'NAME': dburl,
                }

}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.threeandoutfantasyfootball.com','threeandoutfantasyfootball.com','107.22.174.163']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
