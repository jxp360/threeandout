threeandout
===========

Fantasy Football Project

Setup Development Environment
------------------------------
  - Install Python
  - If on Windows, install psychopg2 from `http://www.stickpeople.com/projects/python/win-psycopg/`
  - pip install -r threeandout/requirements/dev.txt
  - cd ./threeandout
  - Set the ENV Variable DJANGO_SETTINGS_MODULE='threeandout.settings.dev'
  - python manage.py runserver