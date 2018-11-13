from django import forms
from .models import Mail

class MailForm(forms.Form):
    date = models.DateTimeField(auto_now_add=True)
    sender = models.EmailField(max_length = 50)
    receiver = models.EmailField(max_length = 50)
    send_mode = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 100)
    body = models.TextField()

    def save(self):
        new_mail = Mail.objects.create(
            date = self.cleaned_data['date'],
            sender = self.cleaned_data['sender'],
            receiver = self.cleaned_data['receiver'],
            send_mode = self.cleaned_data['send_mode'],
            subject = self.cleaned_data['subject'],
            body = self.cleaned_data['body'],
        )
        return new_mail
