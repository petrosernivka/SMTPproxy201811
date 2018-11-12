from django.shortcuts import render
from django.http import HttpResponse

def view_mail(request):
    return render(request, 'view_mail/view_mail.html')
