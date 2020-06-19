from django.shortcuts import render
from testApp.models import Volunteer

# Create your views here.
def registration(request):
    #volunteer=Volunteer.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        password=request.POST['password']
        date=request.POST['date']
        if 'on' in request.POST:
            agreement=False
        else:
            agreement=True
        courses=request.POST.get('course')

        volunteer=Volunteer(name=name,email=email,phoneno=phoneno,password=password,date=date,course=courses,agreement=agreement)
        volunteer.save()
        print('Volunteer Added')

    return render(request,'testApp/index.html')
# Create your views here.
