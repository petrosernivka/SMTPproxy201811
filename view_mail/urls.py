from django.urls import path, include
from django.views.generic import ListView, DetailView
from .views import *

urlpatterns = [
    path('', view_mail, name='view_mail_url'),
    path('mails/<sender>/', mails_list, name='mails_list_url'),
]
