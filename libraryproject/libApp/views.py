from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
# Create your views here.
def home_view(request):
        return render(request,'home.html')
def home1_view(request):
    return render(request,'home1.html')

@login_required
def book_view(request):
    return render(request,'book.html')
@login_required
def media_view(request):
    return render(request,'media.html')
@login_required
def event_view(request):
    return render(request,'event.html')
@login_required
def news_view(request):
    return render(request,'news.html')
@login_required
def photo_gallery_view(request):
    return render(request,'gallery.html')

def contact_view(request):
    return render(request,'contact.html')
@login_required
def library_view(request):
    return render(request,'library.html')
@login_required
def testimonial_view(request):
    return render(request,'testimonial.html')

def register_view(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        #email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Hello user name is already exist!!!')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print('Hello user successfully registered')
                return redirect('/login')
        else:
            messages.info(request,'Hello password not matching')
            return render(request,'register.html')
    else:
        return render(request,'register.html')



def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login')

    else:
        return render(request,'registration/login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('/home')
