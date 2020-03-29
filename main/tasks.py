# ===================================================
# Celery Task/Schedulers
# ===================================================

# standard python
from random import random

# project imports
from .models import *

# celery imports
from celery.decorators import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

import socketio

def send_message(event, data):
    """
    Conección al socket y envio de mensajes
    """
    sio = socketio.Client()
    try:
        sio.connect('http://0.0.0.0:8000', namespaces=['/tasks'])
    except:
        sio.disconnect()
    finally:
        sio.emit(event, data, namespace="/tasks")

# ===================================================
# Tasks
# ===================================================

