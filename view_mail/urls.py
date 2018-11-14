from django.urls import path
from .views import *

urlpatterns = [
    # path('', view_mail, name='view_mail_url'),
    # path('mails/<sender>/', MailView.as_view(), name='mails_list_url'),
    path('', MailView.as_view(), name='mails_list_url'),
]
