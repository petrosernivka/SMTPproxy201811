from django import forms
from .models import Mail_view

class MailForm_view(forms.Form):
    sender = forms.EmailField(max_length = 50)
    password = forms.CharField(widget=forms.PasswordInput)

    sender.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})

    def save(self):
        view_mails = Mail_view.objects.create(
            sender = self.cleaned_data['sender'],
            password = self.cleaned_data['password'],
        )
        return view_mails
