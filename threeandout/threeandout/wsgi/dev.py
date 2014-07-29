"""
WSGI config for threeandout project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('~/.virtualenvs/development/local/lib/python2.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/data/dev/threeandout/threeandout')
sys.path.append('/data/dev/threeandout/threeandout/apps')
sys.path.append('/data/dev/threeandout/threeandout/threeandout')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "threeandout.settings.dev")

# Activate your virtual env
activate_env=os.path.expanduser("~/.virtualenvs/production/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
from django.contrib.auth.handlers.modwsgi import check_password
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

import apache.monitor
apache.monitor.start(interval=1.0)