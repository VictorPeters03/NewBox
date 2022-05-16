from django.db import models


# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=50)
    song = models.CharField(max_length=100)
