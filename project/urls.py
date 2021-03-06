"""djangoscrapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include, url
from rest_framework import routers
from main.views import *

admin.site.site_header = "COVID-19 Screening Assistant"
admin.site.index_title = "Welcome to Dashboard"
admin.site.site_title = "AAAIMX"
admin.site.site_url = "https://www.aaaimx.org/covid19-assistant/"

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"diagnosis", DiagnosticViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
