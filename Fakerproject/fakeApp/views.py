from django.shortcuts import render
from fakeApp.models import School
# Create your views here.
def school_info(request):
    school=School.objects.all()
    return render(request,'fakeApp/home.html',{'school':school})
