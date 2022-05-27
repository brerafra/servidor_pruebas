from .base import *

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['localhost','192.168.11.250']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'