from django.shortcuts import render
from testApp.models import Register
# Create your views here.
def register_view(request):
    return render(request,'testApp/register.html')

def register_form_submission(request):
    print('form submitted')
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']

    register_details=Register(first_name=first_name,last_name=last_name)
    register_details.save()
    return render(request,'testApp/register.html')
