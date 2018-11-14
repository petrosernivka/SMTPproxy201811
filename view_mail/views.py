from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import View
from .forms import MailForm_view
from send_mail.models import Mail

class MailView(View):
    def get(self, request):
        form = MailForm_view()
        return render(request, 'view_mail/view_mail.html', context={'form': form})

    def post(self, request):
        bound_form = MailForm_view(request.POST)
        if bound_form.is_valid():
            sender = bound_form.cleaned_data['sender']
            mails = Mail.objects.filter(sender=sender)
        return render(request, 'view_mail/mail_list.html', context={'mails': mails})
