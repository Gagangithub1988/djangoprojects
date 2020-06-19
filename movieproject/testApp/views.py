from django.shortcuts import render
from . import forms
from testApp.models import MovieInfo
# Create your views here.
def movie_home(request):
    return render(request,'testApp/home.html')

def movie_add(request):
    form=forms.MovieForm()
    if request.method=='POST':
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Data is inserted in Database successfully')
    return render(request,'testApp/addmovie.html',{'form':form})

def movie_list(request):
    movie_list=MovieInfo.objects.all()
    my_dict={'movie_list':movie_list}
    return render(request,'testApp/listmovie.html',context=my_dict)
