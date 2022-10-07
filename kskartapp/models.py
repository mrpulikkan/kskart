from distutils.command import upload
from unicodedata import name
from django.db import models

# Create your models here.
class sample(models.Model):
    pic = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=10)
