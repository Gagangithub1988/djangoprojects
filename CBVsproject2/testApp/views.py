from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from testApp.models import Company
from django.urls import reverse_lazy
# Create your views here.
class list_view(ListView):
    model=Company

class detail_view(DetailView):
    model=Company

class create_view(CreateView):
    model=Company
    fields='cname','clocation','cceo'
class update_view(UpdateView):
    model=Company
    fields=('cname','cceo')
class delete_view(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')
