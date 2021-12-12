from grocery_app.settings import *
import django_heroku
import dj_database_url


django_heroku.settings(locals())
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = ['*', ]

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

STATIC_ROOT = 'static'

DATABASES['default'] = dj_database_url.config()

CELERY_BROKER_URL = config("REDIS_URL")
CELERY_RESULT_BACKEND = config("REDIS_URL")


