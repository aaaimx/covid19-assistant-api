from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
@admin.register(Diagnostic)
class AdminDiagnostic(admin.ModelAdmin):
    list_display = ('id','diagnosis', 'disease', 'values', 'created_at')
    list_filter = ()


