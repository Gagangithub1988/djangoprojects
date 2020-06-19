import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ORMproject1_ver_2.settings')

import django
django.setup()

from testApp.models import Employee
from faker import Faker

fake=Faker()

def populate(n):
    for i in range(n):
        fename=fake.name()
        feno=fake.random_number(digits=3)
        fesal=fake.random_number(digits=5)
        feaddrs=fake.address()
        emp_record=Employee.objects.get_or_create(ename=fename,eno=feno,esal=fesal,eaddrs=feaddrs)

populate(10)
