from django.shortcuts import render
from testApp.models import Employee,ProxyEmployee,ProxyEmployee2
# Create your views here.
def emp_info(request):
    emp_list=Employee.objects.all()
    return render(request,'testApp/index.html',{'emp_list':emp_list})
def proxyemp_info(request):
    emp_list=ProxyEmployee.objects.all()
    return render(request,'testApp/index.html',{'emp_list':emp_list})
def proxyemp_info2(request):
    emp_list=ProxyEmployee2.objects.all()
    return render(request,'testApp/index.html',{'emp_list':emp_list})
