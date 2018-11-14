from django.db import models

class Mail_view(models.Model):
    sender = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.sender
