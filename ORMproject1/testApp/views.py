from django.shortcuts import render
from testApp.models import Employee,ProxyEmployee,ProxyEmployee2
# Create your views here.
def EmployeeInfo(request):
    emp_list=ProxyEmployee.objects.all()
    return render(request,'testApp/home.html',{'emp_list':emp_list})
