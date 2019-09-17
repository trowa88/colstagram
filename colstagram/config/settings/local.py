from .base import *


def get_env(env_name):
    import os
    return os.getenv(env_name)


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'colstagram',
        'USER': 'postgres',
        'PASSWORD': get_env('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
