from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.
def home_view2(request):
    return render(request,'login2App/home2.html')
def login_view2(request):
    a=10
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home2')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login_view2')
    return render(request,'registration/login2.html')

def register_view2(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if 'on' in request.POST:
            messages.info(request,'Please accept our AGREEMENT')
            return redirect('/register_view2')
        else:
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'User already exist')
                    return render(request,'registration/login2.html')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exist')
                    return render(request,'registration/login2.html')
                else:
                    user=User.objects.create_user(first_name=first_name,username=username,email=email,password=password1)
                    user.save()
                    return redirect('/login_view2')

    return render(request,'registration/login2.html')

def logout_view2(request):
    auth.logout(request)
    return redirect('/home2/')
