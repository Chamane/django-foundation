from .common import *

import django_heroku

#import dj_database_url

django_heroku.settings(local())

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)
