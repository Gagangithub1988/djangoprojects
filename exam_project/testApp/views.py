from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testApp.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
# Create your views here.
def home_view(request):
    return render(request,'testApp/home.html')

@login_required
def java_exam_view(request):
    return render(request,'testApp/java.html')
@login_required
def python_exam_view(request):
    return render(request,'testApp/python.html')
@login_required
def sql_exam_view(request):
    return render(request,'testApp/sql.html')

def register_view(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
    return render(request,'testApp/register.html',{'form':form})
