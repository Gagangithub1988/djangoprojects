from django.shortcuts import render
import datetime
# Create your views here.
def tempinfo(request):
    date=datetime.datetime.now()
    name='Tamanna'
    h=int(date.strftime('%H'))
    if h<12:
        msg='Good Morning!!!'
    elif h<16:
        msg='Good Afternoon!!!'
    elif h<22:
        msg='Good Evening!!!'
    else:
        msg='Good Night!!!'
    my_dict={'date':date,'name':name,'msg':msg}
    return render(request,'testApp/hello.html',context=my_dict)
