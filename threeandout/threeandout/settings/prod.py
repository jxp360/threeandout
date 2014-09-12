# Django settings for threeandout project.
from threeandout.settings.common import *
from threeandout.settings.prod_info import *
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'threeandoutfantasyfootball@gmail.com'

db_var_names = ['POSTGRESQL_DB_USER', 'POSTGRESQL_DB_PASSWORD', 'POSTGRESQL_DB_URL']
if not all( i in globals() for i in db_var_names ):
    print "ERROR: DB Variables are not defined: "+str(db_var_names)
    print "       Check that there is a prod_info.py in the settings and"
    print "       "+str(db_var_names)+" are properly defined."
    sys.exit(1)

dburl = '/data/threeandout/dbs/threeandout.db'

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2', 
                'NAME': 'threeandout',
                'USER': POSTGRESQL_DB_USER,
                'PASSWORD': POSTGRESQL_DB_PASSWORD,
                'HOST': POSTGRESQL_DB_URL,
                'PORT': 5432 },
    'slave': {'ENGINE': 'django.db.backends.sqlite3', 
                'NAME': dburl}

}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'threeandout.wsgi.prod.application'

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
