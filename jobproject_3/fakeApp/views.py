from django.shortcuts import render
from fakeApp.models import Hyderabad_jobs,Mumbai_jobs,Pune_jobs,Bangalore_jobs
# Create your views here.
def jobs_info(request):
    return render(request,'jobApp/home.html')

def hyd_jobs_info(request):
    hyd_jobs=Hyderabad_jobs.objects.all()
    return render(request,'fakeApp/hydjobs.html',{'hyd_jobs':hyd_jobs})

def mumbai_jobs_info(request):
    mumbai_jobs=Mumbai_jobs.objects.all()
    return render(request,'fakeApp/mumbaijobs.html',{'mumbai_jobs':mumbai_jobs})

def pune_jobs_info(request):
    pune_jobs=Pune_jobs.objects.all()
    return render(request,'fakeApp/punejobs.html',{'pune_jobs':pune_jobs})

def bangalore_jobs_info(request):
    bangalore_jobs=Bangalore_jobs.objects.all()
    return render(request,'fakeApp/bangalorejobs.html',{'bangalore_jobs':bangalore_jobs})
