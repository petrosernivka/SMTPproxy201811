from django.urls import path, include
from django.views.generic import ListView, DetailView
from view_mail.models import Mails
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
