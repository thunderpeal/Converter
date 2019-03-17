"""
Definition of urls for Converter.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path, include
import django.contrib.auth.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    path("",include("conv.urls"))
    ]
