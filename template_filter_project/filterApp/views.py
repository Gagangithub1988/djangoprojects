from django.shortcuts import render
from filterApp.models import FilterModel
# Create your views here.
def upper_view(request):
    data_list=FilterModel.objects.all()
    data_dic={'data_list':data_list}
    return render(request,'filterApp/upper.html',context=data_dic)

def lower_view(request):
    data_list=FilterModel.objects.all()
    data_dic={'data_list':data_list}
    return render(request,'filterApp/lower.html',context=data_dic)
