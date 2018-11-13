from django.shortcuts import render
from django.http import HttpResponse
from send_mail.models import Mail

def view_mail(request):
    return render(request, 'view_mail/view_mail.html')

def mails_list(request, sender='donkixot21@outlook.com'):
    mails = Mail.objects.filter(sender=sender)
    return render(request, 'view_mail/mail_list.html', context={'mails': mails})
