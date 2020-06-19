from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    cname=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)
    cceo=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
