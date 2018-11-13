from django.urls import path
from .views import send_mail

urlpatterns = [
    path('', send_mail, name='send_mail_url'),
    path('mail/create', MailCreate.as_view(), name='mail_create_url'),
]
