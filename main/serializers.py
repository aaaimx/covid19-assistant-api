# serializers.py
from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        exclude = []