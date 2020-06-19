from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class Helloworld_view(View):
    def get(self,request):
        return HttpResponse('<h1>Hello Gagan</h1>')

class HelloworldTemplate_view(TemplateView):
    template_name='test.html'

class HelloworldTemplateContext_view(TemplateView):
    template_name='test2.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Gagan'
        context['subject']='Python'
        context['marks']=100
        return context
