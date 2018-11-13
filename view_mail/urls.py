from django.urls import path, include
from django.views.generic import ListView, DetailView
from .views import view_mail

urlpatterns = [
    path('', view_mail, name='view_mail_url'),
]
