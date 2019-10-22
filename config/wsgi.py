import os

from django.core.wsgi import get_wsgi_application

# change config.settings.production to config.settings.local if you are running locally
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_wsgi_application()
