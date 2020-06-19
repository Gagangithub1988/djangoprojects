from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    date=models.DateField()
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()
