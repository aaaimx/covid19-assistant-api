# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import dj_database_url
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql'
    }
}

URL = os.environ.get('DATABASE_URL', None)
DATABASES['default'] = dj_database_url.config(default=URL, conn_max_age=60)
