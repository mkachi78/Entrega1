from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Messages(models.Model):

    timestamp = models.DateTimeField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
