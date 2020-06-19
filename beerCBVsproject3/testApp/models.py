from django.db import models
from django.urls import reverse

# Create your models here.
class Beer(models.Model):
    name=models.CharField(max_length=100)
    taste=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
