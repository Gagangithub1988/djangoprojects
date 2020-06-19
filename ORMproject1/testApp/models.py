from django.db import models

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('id')
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=15000)
class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')


# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddress=models.CharField(max_length=100)
    objects=CustomManager1()

class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True
class ProxyEmployee2(Employee):
    objects=CustomManager1()
    class Meta:
        proxy=True
