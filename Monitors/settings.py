# -*- coding: utf-8 -*-
"""
Django settings for Monitors project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p+5!8qls-7ev4%@knzo8)4o_v+53@#_#j8uvt0sb9au60j)n!f'

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
    'TomcatMonitor',
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

ROOT_URLCONF = 'Monitors.urls'

WSGI_APPLICATION = 'Monitors.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': 'voilet_cmdb_v1',  # Or path to database file if using sqlite3.
        'NAME': 'monitor',  # Or path to database file if using sqlite3.
         'USER': 'root',
         'PASSWORD': '123456',  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        "OPTIONS": {
            "init_command": "SET foreign_key_checks = 0;",    #禁用外键约束
        },
    },

    # 'slave': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'salt',
    #     'USER': 'root',
    #     'PASSWORD': 'wanghui',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = 'static/'

STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    ('css', os.path.join(STATIC_ROOT, 'css').replace('\\', '/')),
    ('js', os.path.join(STATIC_ROOT, 'js').replace('\\', '/')),
    ('img', os.path.join(STATIC_ROOT, 'img').replace('\\', '/')),
    ('fonts', os.path.join(STATIC_ROOT, 'fonts').replace('\\', '/')),
    ('extra', os.path.join(STATIC_ROOT, 'extra').replace('\\', '/')),
    ('bootstrap', os.path.join(STATIC_ROOT, 'bootstrap').replace('\\', '/')),
    ('new', os.path.join(STATIC_ROOT, 'new').replace('\\', '/')),
    ('images', os.path.join(STATIC_ROOT, 'images').replace('\\', '/')),
    ('ztree', os.path.join(STATIC_ROOT, 'ztree').replace('\\', '/')),
    ('layer', os.path.join(STATIC_ROOT, 'layer').replace('\\', '/')),
    ('external', os.path.join(STATIC_ROOT, 'external').replace('\\', '/')),
    ('pdf', os.path.join(STATIC_ROOT, 'pdf').replace('\\', '/')),
    ('lib', os.path.join(STATIC_ROOT, 'lib').replace('\\', '/')),
    ('plugins', os.path.join(STATIC_ROOT, 'plugins').replace('\\', '/')),
    ('md', os.path.join(STATIC_ROOT, 'md').replace('\\', '/')),

)

TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)

