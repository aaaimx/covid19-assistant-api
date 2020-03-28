from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from datetime import datetime

# Create your models here.
# class Report(models.Model):
#     label = models.CharField(default="", blank=True, null=True, max_length=100)
#     country = models.CharField(default="", blank=True, null=True, max_length=20)
#     source = models.URLField(default="", blank=True, null=True, max_length=200)
#     data = JSONField(default=None, null=True, blank=True)
#     created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)


