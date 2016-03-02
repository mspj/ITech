"""
Django settings for ITech project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8d=1v29-kjk8#)-dc=(-+_kerva=bv&fh51hgr95$ivn_7as1b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookwormsunite',
    'twitter_tag',
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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'bookwormsunite.context_processors.include_login_form',
    'bookwormsunite.context_processors.include_register_form',
)

# Your access token: Access token
TWITTER_OAUTH_TOKEN = '4925320361-NfqsXqimaoh1w47oRkhLMTfsyMTY5wKVoOJC9KI'
# Your access token: Access token secret
TWITTER_OAUTH_SECRET = 'sYwMWdy0HYYt0suHi7lAqGWBzg5iT0YGx3vXOdfZq9Mub'
# OAuth settings: Consumer key
TWITTER_CONSUMER_KEY = 'jzaX3FpCkrjVLox9WCxdRSeuK'
# OAuth settings: Consumer secret
TWITTER_CONSUMER_SECRET = 'NxRDUo7zKXPVmmK6vKUpHEwxwpmbCg3vx3Nyp0ocr4M4L62QrR'

ROOT_URLCONF = 'ITech.urls'

WSGI_APPLICATION = 'ITech.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'bookwormsunite.Reader'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    STATIC_PATH,
)

# Template files

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SUCCESS_STATUS = 'success'
FAIL_STATUS = 'fail'
SUCCESS_LOGIN_MSG = 'Successfully logged in'
SUCCESS_REGISTER_MSG = 'Successfully registered'
INCORRECT_CREDS_MSG = 'Your username and/or password are incorrect.'
DISABLED_ACC_MSG = 'Your account is disabled.'
