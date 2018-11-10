from django.db import models

class Mails(models.Model):
    date = models.DateTimeField()
    sender = models.CharField(max_lenght = 50)
    receiver = models.CharField(max_lenght = 50)
    send_mode = models.CharField(max_lenght = 50)
    subject = models.CharField(max_lenght = 100)
    body = models.TextField()
