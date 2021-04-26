"""
Django settings for investapp project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import logging
import os
from enum import Enum
from logging.handlers import RotatingFileHandler
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# LOGGING CONFIG

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('findata')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# to log debug messages
debug_logger = logging.StreamHandler()
debug_logger.setLevel(logging.DEBUG)
debug_logger.setFormatter(formatter)

# to log general messages
# x2 files of 2mb
info_logger = RotatingFileHandler(filename='investapp.log', maxBytes=2097152, backupCount=2)
info_logger.setLevel(logging.INFO)
info_logger.setFormatter(formatter)

#to log errors messages
error_logger = RotatingFileHandler(filename='investapp_errors.log', maxBytes=2097152, backupCount=2)
error_logger.setLevel(logging.ERROR)
error_logger.setFormatter(formatter)

logger.addHandler(debug_logger)
logger.addHandler(info_logger)
logger.addHandler(error_logger)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't3=iwr8^i&_dl=68r(7mn#)4j%sq1baao6418amt1=k+hh_0m1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'profiles.apps.ProfilesConfig',
    'markets.apps.MarketsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'investapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),
                 (os.path.join(os.path.join(BASE_DIR, 'profiles'), 'templates'))
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'investapp.context_processors.base_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'investapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'investapp',
        'USER': 'investapp_admin',
        'PASSWORD': 'InvestAppPass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = "profiles.UserProfile"

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_URL = "/profiles/login/"
LOGOUT_REDIRECT_URL = '/index/'

# RISKLEVEL CONSTANTS
RISK_MAX_LVL = 3
RISK_MIN_LVL = 1

RISK_PROFILE = Enum('RISK_PROFILE', 'BAJO MODERADO ALTO')

# The score range from the risk profile test
MAX_TEST_SCORE = 69
MIN_TEST_SCORE = 20

# Precalc of the classification of the user's test score in one of the groups
GROUP_SEGMENT_LENGTH = (MAX_TEST_SCORE - MIN_TEST_SCORE) / len(RISK_PROFILE)
GROUPS_LEFT_LIMITS = Enum('RISK_PROFILE', {'BAJO': MIN_TEST_SCORE,
                                           'MODERADO': (MIN_TEST_SCORE + GROUP_SEGMENT_LENGTH) + 1,
                                           'ALTO': (MIN_TEST_SCORE + 2*GROUP_SEGMENT_LENGTH) + 1})

# Fincalcs connection data

FINCALCS_HOST = 'http://localhost:8001'
FINCALCS_SYMBOLS_ENDPOINT = '/symbols'
FINCALCS_PORTFOLIO_ENDPOINT = '/portfolio'

