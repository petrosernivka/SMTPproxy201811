from django.urls import path
from .views import *

urlpatterns = [
    # path('', send_mail_page, name='send_mail_url'),
    path('', MailCreate.as_view(), name='mail_create_url'),
]
