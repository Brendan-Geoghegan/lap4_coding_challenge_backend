from django.db import models

# Create your models here.
class Urls(models.Model):
    long_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=300)
