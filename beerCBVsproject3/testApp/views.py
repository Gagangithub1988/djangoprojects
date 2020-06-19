from django.shortcuts import render
from testApp.models import Beer
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class list_view(ListView):
    model=Beer

class detail_view(DetailView):
    model=Beer

class create_view(CreateView):
    model=Beer
    fields='__all__'

class update_view(UpdateView):
    model=Beer
    fields='__all__'

class delete_view(DeleteView):
    model=Beer
    success_url=reverse_lazy('beers')
