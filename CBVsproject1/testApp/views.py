from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testApp.models import Book
# Create your views here.
class Booklistview(ListView):
    model=Book

class Bookdetailview(DetailView):
    model=Book
