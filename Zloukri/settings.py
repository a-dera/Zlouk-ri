"""
Django settings for Zloukri project.

Generated by 'django-admin startproject' using Django 2.2. (#Django 3.1.2 now)

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6p3@je0oinc13vkx!73-nr%b!02v$#ug+t1$uks@1b8^7@7_00'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'https://zloukri.herokuapp.com/',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'zlou.apps.ZlouConfig',
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

ROOT_URLCONF = 'Zloukri.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['zlou/template/zlou'],
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

WSGI_APPLICATION = 'Zloukri.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#setuping database to mysql
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST' : 'ec2-52-204-141-94.compute-1.amazonaws.com',
        'NAME' : 'd7pcobmbi14dn0',
        'USER' : 'ulcwyzhvhsdyvh',
        'PORT' : '5432',
        'PASSWORD' : '5e94b2dac493cd90bc438422ef3bd0b98d8d03d9d0e4cc6a845b9d27165514be',
        'URI' : 'postgres://ulcwyzhvhsdyvh:5e94b2dac493cd90bc438422ef3bd0b98d8d03d9d0e4cc6a845b9d27165514be@ec2-52-204-141-94.compute-1.amazonaws.com:5432/d7pcobmbi14dn0',
        'Heroku CLI' : 'heroku pg:psql postgresql-shaped-92344 --app zloukri',
        #'OPTIONS': {
        #   'read_default_file': os.path.join(BASE_DIR, 'configs.cnf'),
        #},
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Activate Django-Heroku.
django_heroku.settings(locals())