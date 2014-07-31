# Django settings for threeandout project.
from threeandout.settings.common import *
from threeandout.settings.prod_info import *
DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'threeandoutfantasyfootball@gmail.com'


DATABASES = {
    'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2', 
                'NAME': 'threeandout',
                'USER': POSTGRESQL_DB_USER,
                'PASSWORD': POSTGRESQL_DB_PASS,
                'HOST': POSTGRESQLD_DB_URL,
                'PORT': 5432 },

}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.threeandoutfantasyfootball.com','threeandoutfantasyfootball.com','54.86.69.247']

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
