from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic import View
from datetime import datetime
from .forms import MailForm
from .models import *

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail_check(m):
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

    try:
        server = SMTP(SMTP_server + ':' + port)
    except Exception:
        return '''Неможливо створити зв'язок з SMTP-сервером'''

    server.starttls()
    try:
        server.login(m.cleaned_data['sender'], m.cleaned_data['password'])
    except Exception:
        return 'Логін або пароль невірний'

    server.quit()
    return 0

def send_mail_ok(m):
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
    email_content = msg.as_string()
    server = SMTP(SMTP_server + ':' + port)
    server.starttls()
    server.login(m.cleaned_data['sender'], m.cleaned_data['password'])
    server.sendmail(m.cleaned_data['sender'], m.cleaned_data['receiver'], email_content)
    server.quit()
    pass

def get_send_mode(sender):
    try:
        return Send_rules.objects.get(sender=sender).send_mode
    except:
        return Send_rules.objects.get(sender='all@all.all').send_mode

class MailCreate(View):
    def get(self, request):
        form = MailForm()
        return render(request, 'send_mail/send_mail.html', context={'form': form})

    def post(self, request):

        # print (request.POST.get('send_mode'))
        # print (bound_form['send_mode'].value())
        # print (bound_form.data['send_mode'])

        bound_form = MailForm(request.POST)

        if bound_form.is_valid():
            bound_form.cleaned_data['send_mode'] = get_send_mode(bound_form.cleaned_data['sender'])
            bound_form.cleaned_data['date'] = datetime.now()
            bound_form.own_err = send_mail_check(bound_form)
            if not bound_form.own_err:
                if bound_form.cleaned_data['send_mode'] == 'OK':
                    send_mail_ok(bound_form)

                elif bound_form.cleaned_data['send_mode'] != 'BLOCK':
                    bound_form.cleaned_data['receiver'] = bound_form.cleaned_data['send_mode']
                    send_mail_ok(bound_form)

                new_mail = bound_form.save()
                # return redirect(mail_create_url)
                # To be able to to pass a model instance to redirect, I need to have defined a get_absolute_url() method on it
                form = MailForm()
                form.success = 'Лист відправлено!'
                return render(request, 'send_mail/send_mail.html', context={'form': form})

        return render(request, 'send_mail/send_mail.html', context={'form': bound_form})
