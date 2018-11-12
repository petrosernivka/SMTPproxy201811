from django.urls import path
from .views import send_mail

urlpatterns = [
    path('', send_mail, name='send_mail'),
]
