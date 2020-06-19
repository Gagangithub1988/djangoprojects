import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Fekerproject.settings')

import django
django.setup()

from fakeApp.models import School
from faker import Faker

fake=Faker()
def populate(n):
    num=1
    for i in range(n):
        name=fake.name()
        rollno=fake.random_number(digits=2)
        addr=fake.address()
        school_record=School.objects.get_or_create(name=name,rollno=rollno,addr=addr)

populate(20)
