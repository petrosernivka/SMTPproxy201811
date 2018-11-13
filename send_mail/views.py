from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import View
from .forms import MailForm

def send_mail_real(request):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import cgi

    form = cgi.FieldStorage()
    sender_email_address = form.getfirst("sender_email_address", "donkixot21@gmail.com")

    # sender_email_address = 'donkixot21@gmail.com'
    sender_email_password = 'dondon-x2'
    receiver_email_address = 'p.sernivka@gmail.com'

    email_subject_line = 'Sample Python Email'

    msg = MIMEMultipart()
    msg['From'] = sender_email_address
    msg['To'] = receiver_email_address
    msg['Subject'] = email_subject_line

    email_body = 'Hello World. This is a Python Email using SMTP server with Outlook service.'
    msg.attach(MIMEText(email_body, 'plain'))

    email_content = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender_email_address, sender_email_password)

    server.sendmail(sender_email_address, receiver_email_address, email_content)
    server.quit()
    pass

class MailCreate(View):
    def get(self, request):
        form = MailForm()
        return render(request, 'send_mail/send_mail.html', context={'form': form})

    def post(self, request):
        bound_form = MailForm(request.POST)

        if bound_form.is_valid():
            new_mail = bound_form.save()
            return redirect(new_mail)

        return render(request, 'send_mail/send_mail.html', context={'form': bound_form})
