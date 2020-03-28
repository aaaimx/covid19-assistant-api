"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import socketio
import eventlet
import eventlet.wsgi
import os
from django.conf import settings

if settings.ENV == 'development':
    from .socket_app import sio
else:
    sio = socketio.Server(async_mode='eventlet', cors_allowed_origins="*")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
application = get_wsgi_application()
application = socketio.WSGIApp(sio, application)

if settings.ENV == 'development':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), application)
