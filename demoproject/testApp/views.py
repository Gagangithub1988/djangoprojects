from django.shortcuts import render


# Create your views here.
def demoview(request):
    return render(request,'testApp/demo.html')
