"""
Django settings for postfixadmin project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
from os.path import abspath, join, normpath

import dj_database_url

PROJECT_ROOT = normpath(join(abspath(__file__), "..", "..", "..",))
REPO_ROOT = normpath(join(PROJECT_ROOT, "..",))

MEDIA_ROOT = normpath(join(PROJECT_ROOT, "media"))
MEDIA_URL = '/media/'

STATIC_ROOT = normpath(join(PROJECT_ROOT, "static"))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    normpath(join(REPO_ROOT, "assets")),
)

TEMPLATE_DIRS = (
    normpath(join(PROJECT_ROOT, "templates")),
)

DATABASES = {
    'default': dj_database_url.config(
        default="sqlite:///{0}".format(normpath(join(REPO_ROOT, "db", "db.sqlite3")))
    )
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Quick-start deve:pment settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['_SECRET_KEY']


SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('_DEBUG', False))

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'pfa.User'

PFA_DEFAULT_MAILDIR = '/var/mail/vmail/'

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'braces',
    'crispy_forms',
    'rest_framework',
    'debug_toolbar.apps.DebugToolbarConfig',
)

LOCAL_APPS = (
    'pfa',
    'api',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
    'rest_framework.serializers.ModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ]
}


ROOT_URLCONF = 'postfixadmin.urls'

WSGI_APPLICATION = 'postfixadmin.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

FIXTURE_DIRS = ('fixtures', )

# Celery
BROKER_URL='redis://127.0.0.1:6379/0'
BROKER_TRANSPORT='redis'


LOG_FILENAME = normpath(join(REPO_ROOT, "logs", "debug.log"))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '[%d/%b/%Y %H:%M:%S]'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': LOG_FILENAME,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'propagate': False,
            'level': 'ERROR',
        },
        'pfa.views': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}
