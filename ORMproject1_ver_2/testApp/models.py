from django.db import models

# Create your models here.
class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ename="Kendra Martin")

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('esal')

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=300)
    esal=models.IntegerField()
    eaddrs=models.CharField(max_length=300)

class ProxyEmployee(Employee):
    objects=CustomManager1()
    class Meta:
        proxy=True

class ProxyEmployee2(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True
