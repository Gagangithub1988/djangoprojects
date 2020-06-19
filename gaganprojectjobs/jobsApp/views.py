from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs(request):
    s='Hyderabad jobs information'
    return HttpResponse(s)
def punejobs(request):
    s='Pune jobs information'
    return HttpResponse(s)
def chennaijobs(request):
    s='Chennai jobs information'
    return HttpResponse(s)
def mumbaijobs(request):
    s='Mumbai jobs information'
    return HttpResponse(s)
