from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=10)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=300)
    salary=models.FloatField()
