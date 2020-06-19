from django.db import models

# Create your models here.
class Hyderabad_jobs(models.Model):
    #Slno=models.Serila()
    date=models.DateTimeField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=256)
    email=models.EmailField()
    phnno=models.IntegerField()
    #class Meta:
        #app_label = 'Hyderabad_jobs'

class Mumbai_jobs(models.Model):
    #Slno=models.IntegerField()
    date=models.DateTimeField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=256)
    email=models.EmailField()
    phnno=models.IntegerField()
    #class Meta:
        #app_label = 'Mumbai_jobs'

class Pune_jobs(models.Model):
    #Slno=models.IntegerField()
    date=models.DateTimeField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=256)
    email=models.EmailField()
    phnno=models.IntegerField()
    #class Meta:
        #app_label = 'Pune_jobs'

class Bangalore_jobs(models.Model):
    #Slno=models.IntegerField()
    date=models.DateTimeField()
    company=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    eligibility=models.CharField(max_length=200)
    address=models.CharField(max_length=256)
    email=models.EmailField()
    phnno=models.IntegerField()
    #class Meta:
        #app_label = 'Bangalore_jobs'
