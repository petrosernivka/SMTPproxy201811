from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic import View
from .forms import MailForm

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail_real(m):
    msg = MIMEMultipart()

    msg['From'] = m.cleaned_data['sender']
    msg['To'] = m.cleaned_data['receiver']
    msg['Subject'] = m.cleaned_data['subject']

    msg.attach(MIMEText(m.cleaned_data['body'], 'plain'))

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

    email_content = msg.as_string()

    try:
        server = SMTP(SMTP_server + ':' + port)
    except Exception:
        return '''Неможливо створити зв'язок з SMTP-сервером'''

    server.starttls()
    try:
        server.login(m.cleaned_data['sender'], m.cleaned_data['password'])
    except Exception:
        return 'Логін або пароль невірний'

    server.sendmail(m.cleaned_data['sender'], m.cleaned_data['receiver'], email_content)
    server.quit()
    return 0

class MailCreate(View):
    def get(self, request):
        form = MailForm()
        return render(request, 'send_mail/send_mail.html', context={'form': form})

    def post(self, request):
        bound_form = MailForm(request.POST)

        if bound_form.is_valid():
            bound_form.own_err = send_mail_real(bound_form)
            if not bound_form.own_err:
                new_mail = bound_form.save()
                # return redirect(mail_create_url)
                # To be able to to pass a model instance to redirect, I need to have defined a get_absolute_url() method on it
                form = MailForm()
                form.success = 'Лист відправлено!'
                return render(request, 'send_mail/send_mail.html', context={'form': form})

        return render(request, 'send_mail/send_mail.html', context={'form': bound_form})
