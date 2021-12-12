web: gunicorn grocery_app.wsgi --log-file -
worker: celery -A grocery_app worker beat -l info --without-gossip --without-mingle --without-heartbeat
release: python manage.py migrate