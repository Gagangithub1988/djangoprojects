from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.

def home_view(request):
    return render(request,'testApp/home.html')

@login_required
def java_view(request):
    return render(request,'testApp/java.html')

def my_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'registration/login.html')
    return render(request,'registration/login.html')
def logout_view(request):
    auth.logout(request)
    return redirect('/my_view')