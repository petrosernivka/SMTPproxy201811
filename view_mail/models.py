from django.db import models

class Mails(models.Model):
    date = models.DateTimeField()
    sender = models.CharField(max_length = 50)
    receiver = models.CharField(max_length = 50)
    send_mode = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 100)
    body = models.TextField()
