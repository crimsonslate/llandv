import logging.config
import os
import socket
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = [
    ".llandv.com",
    "llandv.com",
    "llandv-bucket.s3.amazonaws.com",
    socket.gethostbyname(socket.gethostname()),
]

INSTALLED_APPS = [
    "portfolio.apps.PortfolioConfig",
    "corsheaders",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.postgres",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.forms",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "llandv.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ]
        },
    }
]

WSGI_APPLICATION = "llandv.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Chicago"

USE_I18N = False

USE_TZ = True

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "media/"

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000

WAGTAIL_SITE_NAME = "llandv"

WAGTAILADMIN_BASE_URL = "https://llandv.com"

WAGTAILDOCS_EXTENSIONS = [
    "csv",
    "docx",
    "key",
    "odt",
    "pdf",
    "pptx",
    "rtf",
    "txt",
    "xlsx",
    "zip",
]

SERVER_EMAIL = "server@llandv.com"

DEFAULT_FROM_EMAIL = "noreply@llandv.com"

DEFAULT_REPLY_TO_EMAIL = "bryce@llandv.com"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST")

EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

EMAIL_PORT = os.getenv("EMAIL_PORT", 587)

EMAIL_USE_TLS = True

FILE_CHARSET = "utf-8"

LOGGING_CONFIG = None
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "generic": {
                "format": "%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
                "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
                "class": "logging.Formatter",
            }
        },
        "handlers": {
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "generic",
            }
        },
        "root": {"handlers": ["console"], "level": "WARNING"},
        "loggers": {
            "django.request": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "gunicorn.error": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
        },
    }
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "HOST": os.getenv("DB_HOST"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "PORT": os.getenv("DB_PORT", 5432),
        "OPTIONS": {"client_encoding": "utf-8"},
        "CONN_MAX_AGE": None,
    }
}

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": "llandv-bucket",
            "location": "uploads/",
            "region_name": "us-east-1",
            "querystring_auth": True,
            "querystring_expire": 3600,
            "verify": True,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": "llandv-bucket",
            "location": "static/",
            "region_name": "us-east-1",
            "querystring_auth": True,
            "querystring_expire": 3600,
            "verify": True,
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = False

USE_X_FORWARDED_HOST = True

CORS_ALLOWED_ORIGINS = [
    "https://llandv.com",
    "https://www.llandv.com",
    "https://demo.llandv.com",
]
