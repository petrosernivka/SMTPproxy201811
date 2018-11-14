from django.db import models

class Mail(models.Model):
    date = models.DateTimeField()
    sender = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 20)
    receiver = models.EmailField(max_length = 50)
    send_mode = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 100, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.date.strftime('%Y/%m/%d - %H:%M:%S'), self.sender, self.receiver)
