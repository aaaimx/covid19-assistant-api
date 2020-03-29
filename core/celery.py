# Django Celery
# https://pypi.org/project/django-celery/
import os

CELERY_BROKER_URL = os.environ.get('CLOUDAMQP_URL')
CELERY_IMPORTS = ('main.tasks',)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = "Asia/Calcutta"
