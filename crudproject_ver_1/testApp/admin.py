from django.contrib import admin
from testApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','name','email','address','salary']

admin.site.register(Employee,EmployeeAdmin)
