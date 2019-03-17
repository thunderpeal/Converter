from django.urls import path
from .views import convert

urlpatterns = [
    path("<str:arg1>/<str:arg2>", convert, name = "convert" )
    ]
