from django import forms

class MailForm(forms.Form):
    date = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length = 50)
    receiver = models.CharField(max_length = 50)
    send_mode = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 100)
    body = models.TextField()
