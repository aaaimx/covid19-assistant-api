web: gunicorn -k eventlet -w 1 --threads=5 project.wsgi:application --log-level=debug
worker: celery worker -A project -B --loglevel=INFO --concurrency=5