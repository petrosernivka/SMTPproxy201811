from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import View
from .forms import MailForm

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail_real(m):
    msg = MIMEMultipart()

    msg['From'] = m.cleaned_data['sender']
    msg['To'] = m.cleaned_data['receiver']
    msg['Subject'] = m.cleaned_data['subject']
    
    msg.attach(MIMEText(m.cleaned_data['body'], 'plain'))

    email_content = msg.as_string()
    server = smtplib.SMTP('smtp.outlook.com:587')
    server.starttls()
    server.login(m.cleaned_data['sender'], m.cleaned_data['password'])

    server.sendmail(m.cleaned_data['sender'], m.cleaned_data['receiver'], email_content)
    server.quit()
    pass

class MailCreate(View):
    def get(self, request):
        form = MailForm()
        return render(request, 'send_mail/send_mail.html', context={'form': form})

    def post(self, request):
        bound_form = MailForm(request.POST)

        if bound_form.is_valid():
            send_mail_real(bound_form)
            new_mail = bound_form.save()
            # return redirect(new_mail)
            # To be able to to pass a model instance to redirect, I need to have defined a get_absolute_url() method on it
            return render(request, 'send_mail/send_mail.html', context={'form': bound_form})

        return render(request, 'send_mail/send_mail.html', context={'form': bound_form})
