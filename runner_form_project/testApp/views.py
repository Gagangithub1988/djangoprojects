from django.shortcuts import render
from testApp.models import Runner_Registration

# Create your views here.
def runner_registration_view(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        phone=request.POST['phone']
        dob=request.POST['dob']
        if 'gender' in request.POST:
            genders=request.POST['gender']
        else:
            genders=False
        shirt_sizes=request.POST.get('shirt_size')
        if 'choose_race'in request.POST:
            choose_races=request.POST['choose_race']
        else:
            choose_races=False
        runner=Runner_Registration(name=name,email=email,address=address,city=city,state=state,zip=zip,phone=phone,dob=dob,gender=genders,shirt_size=shirt_sizes,choose_race=choose_races)
        runner.save()
    return render(request,'testApp/runner.html')
