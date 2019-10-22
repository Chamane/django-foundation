import json
from pathlib import Path
from os.path import join

from django.core.exceptions import ImproperlyConfigured

PROJECT_PACKAGE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = str(PROJECT_PACKAGE_DIR.parent)

# JSON Based secret module
try:
 with open('secrets.json') as f:
     secrets = json.loads(f.read())
except IOError:
    secrets = None
    print("Peut pas ouvrir le fichier secrets.json")

def get_secret(setting, secrets=secrets):
    """Get the secret variable or return
       explicit exception
    """

    if secrets is None:
        secrets = {
            "PASSWORD": "password1234",
            "HOST": "127.0.0.1",
            "PORT": "5431"
        }

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

ALLOWED_HOSTS = ['*']

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
MEDIA_ROOT = join(BASE_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = join(BASE_DIR, 'staticfiles')

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like '/home/html/static' or 'C:/www/django/static'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(BASE_DIR, "static")
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'easy_thumbnails',
    'django_user_agents',
    'crispy_forms',

    # Apps DB tables are created in THIS order by default
    # --> Order is CRITICAL to properly handle foreign keys
    'apps.utils',
    'apps.accounts',
    'apps.core',
    'apps.pages',
]



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

USER_AGENTS_CACHE = None

AUTH_USER_MODEL = "accounts.User"

LOGOUT_REDIRECT_URL = "home"
