from django import forms
from datetime import datetime, timedelta
from .models import Mail

class MailForm(forms.Form):
    CHOICES=[('select1','зберегти в базу і переслати далі'),
            ('select2','зберегти в базу, але переслати на інші задані email'),
            ('select3','зберегти в базу і блокувати подальшу передачу')]
    date = forms.DateTimeField()
    sender = forms.EmailField(max_length = 50)
    receiver = forms.EmailField(max_length = 50)
    send_mode = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), initial=('select1','зберегти в базу і переслати далі'))
    subject = forms.CharField(max_length = 100)
    body = forms.CharField()

    sender.widget.attrs.update({'class': 'form-control'})
    receiver.widget.attrs.update({'class': 'form-control'})
    subject.widget.attrs.update({'class': 'form-control'})
    body.widget.attrs.update({'class': 'form-control'})
    date.widget.attrs.update({'value': datetime.now()})

    def clean_date(self):
        new_date = self.cleaned_data['date']
        return new_date

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
