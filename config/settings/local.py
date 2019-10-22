import json

from .common import *

DEBUG = True

# JSON Based secret module
try:
 with open('secrets.json') as f:
     secrets = json.loads(f.read())
except IOError:
    secrets = {
        "PASSWORD": "password1234",
        "DATABASES_HOST": "127.0.0.1",
        "PORT": "5431"
    }
    print("Peut pas ouvrir le fichier secrets.json utilise des valeurs par défaut")

def get_secret(setting, secrets=secrets):
    """Get the secret variable or return
       explicit exception
    """

    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environement variable".format(setting)
        raise ImproperlyConfigured(error_msg)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'oribase',
        'USER': 'postgres',
        'PASSWORD': get_secret("PASSWORD"),
        'HOST': get_secret("DATABASES_HOST"),
        'PORT': get_secret("PORT"),
    }
}
