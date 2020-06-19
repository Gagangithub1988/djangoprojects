import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ORMproject2_ver_2.settings')

import django
django.setup()

from faker import Faker
from testApp.models import Student,Teacher

fake=Faker()

def populate(n):
    for i in range(n):
        fsname=fake.name()
        ftname=fake.name()
        fsemail=fake.email()
        ftemail=fake.email()
        fsaddress=fake.address()
        ftaddress=fake.address()
        frollno=fake.random_number(digits=3)
        fmarks=fake.random_number(digits=2)
        fsubject=fake.random_element(elements=('Odiya','English','Math','Physics','Chemistry','EMW'))
        fsalary=fake.random_number(digits=5)
        student_record=Student.objects.get_or_create(name=fsname,email=fsemail,address=fsaddress,rollno=frollno,marks=fmarks)
        teacher_record=Teacher.objects.get_or_create(name=ftname,email=ftemail,address=ftaddress,subject=fsubject,salary=fsalary)

populate(10)
