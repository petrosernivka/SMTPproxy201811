from django.urls import path, include
from .views import mainApp

urlpatterns = [
    path('', mainApp, name='mainApp_url'),
]
