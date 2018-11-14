from django.urls import path
from .views import *

urlpatterns = [
    path('', MailCreate.as_view(), name='mail_create_url'),
]
