
from django.db import models

# Create your models here.
class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-name')
class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(salary__gte=15000)

class Contactinfo(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField()
    address=models.CharField(max_length=300)
    class Meta:
        abstract=True

class Student(Contactinfo):
    rollno=models.IntegerField()
    marks=models.FloatField()

class Teacher(Contactinfo):
    subject=models.CharField(max_length=200)
    salary=models.FloatField()

class ProxyTeacher(Teacher):
    objects1=CustomManager1()
    objects2=CustomManager2()
    objects3=CustomManager3()
    class Meta:
        proxy=True
