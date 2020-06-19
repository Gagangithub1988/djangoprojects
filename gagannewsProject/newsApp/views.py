from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'newsApp/home.html')

def moviesinfo(request):
    msg_main='latest Movies Informations'
    msg1='Marvell-Captain'
    msg2='Gagan going to release a movies'
    msg3='Kajol love scene is my favourite'
    my_dict={'msg_main':msg_main,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsinfo(request):
    msg_main='latest Sports Informations'
    msg1='Sachin is the best'
    msg2='Dada is the great sixer'
    msg3='Kapil is a legend for India'
    my_dict={'msg_main':msg_main,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
    return render(request,'newsApp/news.html')

def politicsinfo(request):
    msg_main='latest Politics Informations'
    msg1='Corona virus impacting a lot to Ittaly'
    msg2='Subroto Bagchi leading odisha to control corona virus '
    msg3='Please stay at home and support to Govt.'
    my_dict={'msg_main':msg_main,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsApp/news.html',context=my_dict)
    return render(request,'newsApp/news.html')
