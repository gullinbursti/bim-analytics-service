"""
Django settings for bimanalytics project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from bimcore.conf import get_local_conf_dir
import os
import sys


CONFIG_DIR = get_local_conf_dir(
    env_var='BIMANALYTICS_CONFIG_DIR', prod_conf_dir='/etc/bimanalytics')
if CONFIG_DIR not in sys.path:
    # pylint: disable=superfluous-parens
    print('Appending \'{}\' to sys.path.'.format(CONFIG_DIR))
    sys.path.append(CONFIG_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'selfieclub',
)

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
    # TODO: MUST change DEFAULT_PERMISSION_CLASSES!!!
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100,
}

ROOT_URLCONF = 'bimanalytics.urls'
WSGI_APPLICATION = 'bimanalytics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(CONFIG_DIR, 'mysql-django.cnf'),
            'init_command': 'SET storage_engine=INNODB',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.abspath('.'), "static")

# Celery configuration
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Things that need to be in 'local_settings':
#     - SECRET_KEY
#     - AWS_CREDENTIALS
try:
    from local_settings import *  # noqa # pylint: disable=wildcard-import, import-error
except ImportError as original:
    raise ImportError(
        original,
        'There were issues importing local_settings.py.  Are you sure it is '
        'in BIMANALYTICS_CONFIG_DIR\'s \'{}\' directory?'.format(CONFIG_DIR))
