import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Fekerproject.settings')

import django
django.setup()

from fakeApp.models import Hyderabad_jobs,Mumbai_jobs,Pune_jobs,Bangalore_jobs
from faker import Faker
import random
fake=Faker()
def phonenumbergen():
    p=random.randint(7,9)
    num=''+str(p)
    for i in range(9):
        num=num+str(random.randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Team lead','Project Manager','Senior Engineer','Software Developer'))
        feligibility=fake.random_element(elements=('B-Tech','M-Tech','MCA'))
        faddress=fake.address()
        femail=fake.email()
        fphnno=phonenumbergen()
        Hyderabad_jobs_record=Hyderabad_jobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phnno=fphnno)
populate(25)
