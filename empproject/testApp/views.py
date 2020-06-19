from django.shortcuts import render
from testApp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count

# Create your views here.
def empinfo(request):
    emp_list=Employee.objects.all().order_by('esal')[0:3]
    #qs1=Employee.objects.filter(esal__lt=15000)
    #qs2=Employee.objects.filter(ename__endswith='n')
    #emp_list=qs1.union(qs2)
    my_dict={'emp_list':emp_list}
    return render(request,'testApp/emp.html',context=my_dict)

def display_view(request):
    empavg=Employee.objects.all().aggregate(Avg('esal'))
    empmax=Employee.objects.all().aggregate(Max('esal'))
    empmin=Employee.objects.all().aggregate(Min('esal'))
    empsum=Employee.objects.all().aggregate(Sum('esal'))
    empcount=Employee.objects.all().aggregate(Count('esal'))
    return render(request,'testApp/aggregate.html',{'empavg':empavg,'empmax':empmax,'empmin':empmin,'empsum':empsum,'empcount':empcount})
