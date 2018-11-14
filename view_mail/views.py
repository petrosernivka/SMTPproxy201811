from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import View
from .forms import MailForm_view
from send_mail.models import Mail

from smtplib import SMTP

class MailView(View):
    def get(self, request):
        form = MailForm_view()
        return render(request, 'view_mail/view_mail.html', context={'form': form})

    def post(self, request):
        bound_form = MailForm_view(request.POST)
        if bound_form.is_valid():
            bound_form.own_err = mail_authent(bound_form)
            if not bound_form.own_err:
                sender = bound_form.cleaned_data['sender']
                mails = Mail.objects.filter(sender=sender).order_by('-date')
                return render(request, 'view_mail/mail_list.html', context={'mails': mails})
            return render(request, 'view_mail/view_mail.html', context={'form': bound_form})

def mail_authent(m):
    smtp_servers_list = open('smtp_servers.txt')
    domen = m.cleaned_data['sender'][m.cleaned_data['sender'].find('@'):]
    SMTP_server = ''
    for line in smtp_servers_list:
        if line[:line.find('-')] == domen:
            SMTP_server = line[line.find('-') + 1: line.rfind('-')]
            port = line[line.rfind('-') + 1: -2]
    smtp_servers_list.close()
    if not SMTP_server:
        return 'SMTP-сервер для Вашого e-mail не знайдений'

    server = SMTP(SMTP_server + ':' + port)
    server.starttls()
    try:
        server.login(m.cleaned_data['sender'], m.cleaned_data['password'])
    except Exception:
        return 'Логін або пароль невірний'

    server.quit()
    return 0
