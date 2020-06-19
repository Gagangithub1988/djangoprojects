from django.shortcuts import render,redirect
from testApp.models import Employee
from testApp.forms import EmployeeForm
# Create your views here.
def employee_info(request):
    employee_list=Employee.objects.all()
    return render(request,'testApp/home.html',{'employee_list':employee_list})
def employee_addinfo(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'testApp/update.html',{'form':form})

def employee_info_delete(request,id):
    id=int(id)
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/home')

def employee_info_update(request,id):
    id=int(id)
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'testApp/update1.html',{'employee':employee})
