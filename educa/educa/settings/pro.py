from .base import *

DEBUG = False

ADMINS = (("ValSL", "valid.saley@gmail.com"),)

ALLOWED_HOSTS = [".educaproject.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "django_by_example_e_learning",
        "USER": "django_by_example_user",
        "PASSWORD": "etereg14",
        "HOST": "localhost",
        "PORT": "",
    }
}

SECURE_SSL_REDIRECT = True  # должны ли HTTP-запросы перенаправляться на HTTPS
CSRF_COOKIE_SECURE = True