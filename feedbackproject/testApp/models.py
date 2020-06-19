from django.db import models

# Create your models here.
class Volunteer(models.Model):
    fullname=models.CharField(max_length=30)
    