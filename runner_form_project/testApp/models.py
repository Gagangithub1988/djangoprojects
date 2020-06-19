from django.db import models

# Create your models here.
class Runner_Registration(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zip=models.IntegerField()
    phone=models.IntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=30)
    shirt_size=models.CharField(max_length=30)
    choose_race=models.CharField(max_length=30)
