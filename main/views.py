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
from project.settings import DEBUG
from .models import Diagnostic
from .diagnosis import get_diagnosis

# ===================================================
# viesets
# ===================================================
class DiagnosticViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Diagnostics to be viewed or edited.
    """
    queryset = Diagnostic.objects.none()
    serializer_class = DiagnosticSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        values = data.get('values', [])
        diagnosis, disease = get_diagnosis(values)
        print(diagnosis, disease)
        data = {
            'diagnosis': diagnosis,
            'disease': disease,
            'values': ''.join([str(val) for val in values])
        }
        try:
            Diagnostic.objects.create(**data)
        except Exception as err:
            print(err)
        return JsonResponse(data)

        


