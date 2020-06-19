from django.db import models

# Create your models here.
class Rastaurant_Feedback(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    location=models.CharField(max_length=20)
    date=models.DateField()
    time=models.TimeField()
    dine=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    foodq=models.CharField(max_length=20)
    services=models.CharField(max_length=20)
    price=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    comment=models.TextField(max_length=256)
