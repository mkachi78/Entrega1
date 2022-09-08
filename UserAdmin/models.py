from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='profile', null=True, blank=True)
    webpage = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
