from django.shortcuts import render
from testApp.models import Employee

# Create your views here.
def home_view(request):
    employee=Employee.objects.all()
    return render(request,'testApp/home.html',{'employee':employee})