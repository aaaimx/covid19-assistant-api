from django.db import models
from uuid import uuid4
from datetime import datetime

# Create your models here.
class Diagnostic(models.Model):
    result = models.IntegerField(default=0, blank=True, null=True)
    disease = models.CharField(default="", blank=True, null=True, max_length=20)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)


