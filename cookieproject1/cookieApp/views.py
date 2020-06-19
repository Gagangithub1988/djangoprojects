from django.shortcuts import render

# Create your views here.
'''def count_view(request):
    count=int(request.COOKIES.get('count',0))
    new_count=count+1
    response=render(request,'cookieApp/cookie.html',{'count':new_count})
    response.set_cookie('count',new_count,max_age=60)
    return response'''

def name_view(request):
    return render(request,'cookieApp/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'cookieApp/age.html')
    response.set_cookie('name',name)
    return response
