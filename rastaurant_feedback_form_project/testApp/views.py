from django.shortcuts import render
from testApp.models import Rastaurant_Feedback

# Create your views here.
def feedback_view(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        locations=request.POST.get('location')
        date=request.POST['date']
        time=request.POST['time']
        if 'dine' in request.POST:
            dine=request.POST['dine']
        else:
            dine=False
        ages=request.POST.get('age')
        if 'foodq' in request.POST:
            foodq=request.POST['foodq']
        else:
            foodq=False
        if 'service' in request.POST:
            services=request.POST['service']
        else:
            services=False
        if 'price' in request.POST:
            price=request.POST['price']
        else:
            price=False
        if 'experience' in request.POST:
            experience=request.POST['experience']
        else:
            experience=False
        comment=request.POST['comment']

        feedback=Rastaurant_Feedback(fname=fname,lname=lname,email=email,location=locations,date=date,time=time,dine=dine,age=ages,foodq=foodq,services=services,price=price,experience=experience,comment=comment)
        feedback.save()
        print('Feedback Submitted')

    return render(request,'testApp/rastaurant.html')
