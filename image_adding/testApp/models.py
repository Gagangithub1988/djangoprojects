from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=60)
    eprofile_pic=models.ImageField(upload_to='pics')

