from django.shortcuts import render
from Email_send.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
#DataFlair #Send Email
def mail(request):
    subject="Real Programmer Welcome"
    msg="Congratulations for mail"
    to="djangopython1988@gmail.com"
    res=send_mail(subject, msg,EMAIL_HOST_USER,[to,])
    if(res==1):
        msg="Mail sent"
    else:
        msg="Mail couldn't send"
    return HttpResponse(msg)
