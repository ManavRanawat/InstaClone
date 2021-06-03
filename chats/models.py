from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Chat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE,related_name='receiver')

    def __str__(self):
        return self.user1.username+' '+self.user2.username

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField(blank=True)
    date = models.DateField(default = timezone.now)