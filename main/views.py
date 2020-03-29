from .serializers import *
from .models import *

# django imports
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# thirty part
from rest_framework.decorators import action
from rest_framework import viewsets
from project.socket_app import sio
from project.settings import  DEBUG

# ===================================================
# viesets
# ===================================================