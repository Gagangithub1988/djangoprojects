from django.shortcuts import render,redirect
from jobApp.models import Hyderabad_jobs,Mumbai_jobs,Pune_jobs,Bangalore_jobs
from jobApp.forms import hydjobsForm,punejobsForm,mumbaijobsForm,bangalorejobsForm
# Create your views here.
def jobs_info(request):
    return render(request,'jobApp/home.html')

def hyd_jobs_info(request):
    hyd_jobs=Hyderabad_jobs.objects.all()
    return render(request,'jobApp/hydjobs.html',{'hyd_jobs':hyd_jobs})

def addhyd_jobs_info(request):
    form=hydjobsForm()
    if request.method=='POST':
        form=hydjobsForm(request.POST)
        form.save()
        return redirect('/home')
    return render(request,'jobApp/addhydjobs.html',{'form':form})

def mumbai_jobs_info(request):
    mumbai_jobs=Mumbai_jobs.objects.all()
    return render(request,'jobApp/mumbaijobs.html',{'mumbai_jobs':mumbai_jobs})

def addmumbai_jobs_info(request):
    form=mumbaijobsForm()
    if request.method=='POST':
        form=mumbaijobsForm(request.POST)
        form.save()
        return redirect('/home')
    return render(request,'jobApp/addmumbaijobs.html',{'form':form})

def pune_jobs_info(request):
    pune_jobs=Pune_jobs.objects.all()
    return render(request,'jobApp/punejobs.html',{'pune_jobs':pune_jobs})

def addpune_jobs_info(request):
    form=punejobsForm()
    if request.method=='POST':
        form=punejobsForm(request.POST)
        form.save()
        return redirect('/home')
    return render(request,'jobApp/addpunejobs.html',{'form':form})

def bangalore_jobs_info(request):
    bangalore_jobs=Bangalore_jobs.objects.all()
    return render(request,'jobApp/bangalorejobs.html',{'bangalore_jobs':bangalore_jobs})

def addbangalore_jobs_info(request):
    form=bangalorejobsForm()
    if request.method=='POST':
        form=bangalorejobsForm(request.POST)
        form.save()
        return redirect('/home')
    return render(request,'jobApp/addbangalorejobs.html',{'form':form})
