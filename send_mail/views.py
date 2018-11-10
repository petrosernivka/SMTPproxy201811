from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'send_mail/send_mail.html')
