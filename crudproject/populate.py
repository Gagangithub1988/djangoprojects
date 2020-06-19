import os
from django.conf import settings
settings.configure()
os.environ.setdefault('DJANO_SETTINGS_MODULE','crudproject.settings')
import django
django.setup()

from testApp.models import *
from faker import Faker
import random
faker=Faker()
def populate(n):
    for i in range(n):
        feno=random.randint(1001,9999)
        fename=faker.name()
        fesal=random.randint(10000,20000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
populate(20)
