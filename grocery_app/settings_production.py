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

# admin
SERVER_EMAIL = config('ADMIN_EMAIL')

ADMINS = [
    (config('ADMIN_NAME'), config('ADMIN_EMAIL')),
]

# Media storages

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# SMTP Email servier

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('SENDGRID_SERVER')
EMAIL_PORT = config('SENDGRID_PORT')
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = SERVER_EMAIL
