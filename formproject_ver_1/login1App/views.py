from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.
def register_view1(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if 'on' in request.POST:
            messages.info(request,'Please accept our AGREEMENT')
            return redirect('/register_view1')
        else:
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'User is already exist')
                    return render(request,'login1App/index.html')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email is already exist')
                    return render(request,'login1App/index.html')
                else:
                    user=User.objects.create_user(first_name=first_name,email=email,username=username,password=password1)
                    user.save()
                    return redirect('/login_view1/')

    return render(request,'login1App/index.html')

def login_view1(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home1/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login_view1/')

    return render(request,'registration/login.html')

def logout_view1(request):
    auth.logout(request)
    return redirect('/home1/')

def home_view1(request):
    return render(request,'login1App/home1.html')
