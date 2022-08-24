import email
from pyexpat import model
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=40)

class Publication(models.Model):
    author = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    content = models.CharField(max_length=40)

