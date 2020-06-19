from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    class Meta:
        abstract=True

class Student(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()
class Teacher(ContactInfo):
    subject=models.CharField(max_length=100)
    salary=models.FloatField()
class ContactInfo1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)


class Student1(ContactInfo1):
    rollno=models.IntegerField()
    marks=models.IntegerField()
class Teacher1(ContactInfo1):
    subject=models.CharField(max_length=100)
    salary=models.FloatField()
