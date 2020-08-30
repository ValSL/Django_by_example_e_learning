from .base import *

DEBUG = False

ADMINS = (("ValSL", "valid.saley@gmail.com"),)

ALLOWED_HOSTS = ["educaproject.com", "www.educaproject.com"]

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