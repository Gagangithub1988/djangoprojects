import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ORMproject1.settings')
import django
django.setup()

from testApp.models import Employee
from faker import Faker

fake=Faker()

def populate(n):
    for i in range(n):
        feno=fake.random_number(digits=3)
        fename=fake.name()
        fesal=fake.random_number(digits=5)
        feaddress=fake.address()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddress=feaddress)

populate(25)
