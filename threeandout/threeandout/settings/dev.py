# Django settings for threeandout project.
from threeandout.settings.common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

if DEBUG:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'threeandoutfantasyfootball@gmail.com'

dburl = '/data/test/threeandout/dbs/threeandout.db'
import os
if os.environ.has_key('THREEANDOUT_DB'):
    dburl = os.environ['THREEANDOUT_DB']
print 'DBURL = %s' % dburl
DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 
                'NAME': dburl}
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'threeandout.wsgi.dev.application'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# more details on how to customize your logging configuration.
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
            'propagate': False,
        },
    }
}
