from .base import *

MEDIA_DIR = BASE_DIR / 'media'

SECRET_KEY = 'django-insecure-6nj1f*(l6hz=xve3l8n+7e&aezuvp-4qn(d6v%=s5t1ms2uzlv'

DEBUG = True


ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

MEDIA_URL= '/media/'
MEDIA_ROOT = MEDIA_DIR