from django.db import models

from django.contrib.auth.models import User

class Pages (models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    title = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    content = models.CharField(max_length=40)
    date_create = models.DateField()
    imagen = models.ImageField()
