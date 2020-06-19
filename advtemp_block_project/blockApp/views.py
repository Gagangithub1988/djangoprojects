from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'blockApp/home.html')

def movie_view(request):
    return render(request,'blockApp/movie.html')

def sports_view(request):
    return render(request,'blockApp/sports.html')

def politics_view(request):
    return render(request,'blockApp/politics.html')
