from django.shortcuts import render

# Create your views here.
def website_feedback_view(request):
    return render(request,'testApp/website.html')
