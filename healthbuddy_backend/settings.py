"""
Django settings for healthbuddy_backend project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

from decouple import config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-entrypoint.sh development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="set your secret key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# system libs
INSTALLED_APPS += [
    "rest_framework",
    "corsheaders",
    "django_filters",
    "drf_yasg",
    "django_rest_passwordreset",
    "storages",
]

# system apps
INSTALLED_APPS += [
    "healthbuddy_backend.users.apps.UsersConfig",
    "healthbuddy_backend.posts",
    "healthbuddy_backend.articles",
    "healthbuddy_backend.fake_news",
    "healthbuddy_backend.videos",
    "healthbuddy_backend.proxy",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "healthbuddy_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "healthbuddy_backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="healthbuddy"),
        "USER": config("POSTGRES_USER", default="ilha_healthbuddy"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="ilha102030"),
        "HOST": config("POSTGRES_HOST", default="db"),
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# todo: put this to dev
# STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework_simplejwt.authentication.JWTAuthentication"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
}

# DJANGO REST PASSWORD RESET
DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME = 1
DJANGO_REST_PASSWORDRESET_TOKEN_CONFIG = {
    "CLASS": "django_rest_passwordreset.tokens.RandomStringTokenGenerator",
    "OPTIONS": {"min_length": 10, "max_length": 10},
}

# CORS
CORS_ORIGIN_ALLOW_ALL = True

# SENDGRID
SENDGRID_API_KEY = config("SENDGRID_API_KEY", default="set key sendgrid api")
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

# EMAIL
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="emaildefault@mail.com")
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_USE_TLS = True

# RAPIDPRO CONFIG
TOKEN_ORG_RAPIDPRO = config("TOKEN_ORG_RAPIDPRO", default="set token org rapidpro")

# AWS S3
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", default="set access key")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", default="set secret access key")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", default="set storage bucket name")
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME", default="set region name")

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"

AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

STATICFILES_STORAGE = "healthbuddy_backend.storage_backends.StaticStorage"
AWS_PUBLIC_MEDIA_LOCATION = "media/public"
DEFAULT_FILE_STORAGE = "healthbuddy_backend.storage_backends.PublicMediaStorage"
AWS_PRIVATE_MEDIA_LOCATION = "media/private"
PRIVATE_FILE_STORAGE = "healthbuddy_backend.storage_backends.PrivateMediaStorage"

# GOOGLE API AUTH
GOOGLE_API_KEY_FILENAME = config("GOOGLE_API_KEY_FILENAME", default="client_secrets.json")
GOOGLE_API_KEY_FILE_PATH = os.path.join(BASE_DIR, GOOGLE_API_KEY_FILENAME)
GOOGLE_API_PROFILE_ID = config("GOOGLE_API_PROFILE_ID")
