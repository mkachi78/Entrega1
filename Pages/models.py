from django.db import models

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import ForeignKey


class Pages (models.Model):
    author = ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    content = RichTextField()
    date_create = models.DateField()
    imagen = models.ImageField()
