from django import forms
from datetime import datetime
from .models import Mail

class MailForm(forms.Form):
    date = forms.DateTimeField()
    sender = forms.EmailField(max_length = 50)
    password = forms.CharField(widget=forms.PasswordInput)
    receiver = forms.EmailField(max_length = 50)
    send_mode = forms.CharField(max_length = 50, required=False)
    subject = forms.CharField(max_length = 100, required=False)
    body = forms.CharField(required=False)

    sender.widget.attrs.update({'class': 'form-control'})
    receiver.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    subject.widget.attrs.update({'class': 'form-control'})
    body.widget.attrs.update({'class': 'form-control'})
    date.widget.attrs.update({'value': datetime.now(), 'style': 'visibility:hidden'})

    def save(self):
        new_mail = Mail.objects.create(
            date = self.cleaned_data['date'],
            sender = self.cleaned_data['sender'],
            password = self.cleaned_data['password'],
            receiver = self.cleaned_data['receiver'],
            send_mode = self.cleaned_data['send_mode'],
            subject = self.cleaned_data['subject'],
            body = self.cleaned_data['body'],
        )
        return new_mail
