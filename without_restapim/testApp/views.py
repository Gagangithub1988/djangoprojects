from django.shortcuts import render
from django.views.generic import View
from testApp.models import Employee
from django.http import HttpResponse
import json
from testApp.utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testApp.forms import EmployeeForm
#from django.core.serializers import serialize
from testApp.mixins import SerializeMixin,HttpResponseMixin
# Create your views here.
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             json_data=json.dumps({'msg':'The requested resouces not available'})
#             #return HttpResponse(json_data,content_type='application/json',status=404)
#             return self.render_to_http_response(json_data,status=404)
#         else:

#         # emp_data={
#         #     'eno':emp.eno,
#         #     'ename':emp.ename,
#         #     'esal':emp.esal,
#         #     'eaddr':emp.eaddr
#         # }
#         # json_data=json.dumps(emp_data)
#             json_data=self.serialize([emp,])
#            # return HttpResponse(json_data,content_type='application/json',status=200)
#             return self.render_to_http_response(json_data)
#     def get_object_by_id(self,id):
#         try:
#             emp=Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             emp=None
#         return emp

#     def put(self,request,id,*args,**kwargs):
#         emp=self.get_object_by_id(id)
#         if emp is None:
#             json_data=json.dumps({'msg':'No matched resources found,Not possible updation'})
#             return self.render_to_http_response(json_data,status=404)
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'Please send valid json data'})
#             return self.render_to_http_response(json_data,status=400)
#         provided_data=json.loads(data)
#         original_data={
#             'eno':emp.eno,
#             'ename':emp.ename,
#             'esal':emp.esal,
#             'eaddr':'emp.addr',
#         }
#         original_data.update(provided_data)
#         form= EmployeeForm(original_data,instance=emp)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'Resources updated successfully'})
#             return self.render_to_http_response(json_data)
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)

#     def delete(self,request,id,*args,**kwargs):
#         emp=self.get_object_by_id(id)
#         if emp is None:
#             json_data=json.dumps({'msg':'No matched resources found,Not possible deletion'})
#             return self.render_to_http_response(json_data,status=400)
#         status,deleted_item=emp.delete()
#         if status==1:
#             json_data=json.dumps({'msg':'Resources deleted successfully'})
#             return self.render_to_http_response(json_data)
#         json_data=json.dumps({'msg':'Unable to delete pls try again'})
#         return self.render_to_http_response(json_data,status=400)

        


# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
#     def get(self,request,*args,**kwargs):
#         qs=Employee.objects.all()
#         json_data=self.serialize(qs)
#         return HttpResponse(json_data,content_type=('application/json'))
    
#     def post(self,request,*args,**kwargs):
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#             json_data=json.dumps({'msg':'Please send valid data'})
#             return self.render_to_http_response(json_data,status=400)
#         emp_data=json.loads(data)
#         form=EmployeeForm(emp_data)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'Resources created'})
#             return self.render_to_http_response(json_data)
#         if form.errors:
#             json_data=json.dumps(form.errors)
#             return self.render_to_http_response(json_data,status=400)
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCrudCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
    def get(self,request,*args,**kwargs):
        data=request.body
        print(data)
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid data'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'Requested resources not availble with this matched id'})
                return self.render_to_http_response(json_data,status=400)
            json_data=self.serialize([emp,])
            return self.render_to_http_response(json_data)
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)
    
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid data'})
            return self.render_to_http_response(json_data,status=400)
        emp_data=json.loads(data)
        form=EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resources created'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'Requested resources not availble with this matched id'})
                return self.render_to_http_response(json_data,status=400)
            provided_data=json.loads(data)
            original_data={
                'eno':emp.eno,
                'ename':emp.ename,
                'esal':emp.esal,
                'eaddr':emp.eaddr,
            }
            original_data.update(provided_data)
            form= EmployeeForm(original_data,instance=emp)
            if form.is_valid():
                form.save(commit=True)
                json_data=json.dumps({'msg':'Resources updated successfully'})
                return self.render_to_http_response(json_data)
            if form.errors:
                json_data=json.dumps(form.errors)
                return self.render_to_http_response(json_data,status=400)

            


       
