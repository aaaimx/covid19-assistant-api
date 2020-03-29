# -*- coding: utf-8 -*-

# Socket.io settings for Django App
# https://python-socketio.readthedocs.io/en/latest/

from django.conf import settings
from random import random
import socketio
import os

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins="*")

if not settings.ENV == 'development':
    # en desarrollo es necesario correr socket.io server
    # aqui debido a cambio en los archivos
    from project.wsgi import sio

# ===================================================
# Clients
# ===================================================

# Namespace for Celery tasks
@sio.on('connect', namespace='/tasks')
def connect(sid, environ):
    """
    Escucha conecciones en un canal
    """
    print("connect for tasks: ", sid)

#Listining on namespace 
@sio.on('book',namespace='/tasks')
def metrics(sid, book):
    """
    Envia alerta de nuevos libros
    """
    # emiitir mensajes
    sio.emit('chat message', book, namespace='/client')
    print("message ", book)

# ===================================================
# Disconnections
# ===================================================

@sio.on('disconnect')
def disconnect(sid):
    """
    Escucha desconecciones en todos los canales
    """
    print('disconnect ', sid)
