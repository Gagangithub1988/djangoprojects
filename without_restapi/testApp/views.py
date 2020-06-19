from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp_data_view(request):
    emp_data={'eno':100,'ename':'Gagan','esal':30000}
    resp='<h1>Employee No:{}<br>Employee Name:{}<br>EMployee Salary:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data={'eno':100,'ename':'Gagan','esal':30000}
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

#Rarely using below
from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={'eno':100,'ename':'Gagan','esal':30000}
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

#Class Based View
from django.views.generic import View
from testApp.mixins import HttpResponseMixin
class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This response from get method'})
        return self.render_to_http_response(json_data)
        #return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This response from post method'})
        return self.render_to_http_response(json_data)
        #return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This response from put method'})
        return self.render_to_http_response(json_data)
        #return HttpResponse(json_data,content_type='application/json')

    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This response from delete method'})
        return self.render_to_http_response(json_data)
       # return HttpResponse(json_data,content_type='application/json')