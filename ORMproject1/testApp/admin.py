from django.contrib import admin
from testApp.models import Employee,ProxyEmployee,ProxyEmployee2
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddress']
class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddress']
class ProxyEmployeeAdmin1(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddress']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee2,ProxyEmployeeAdmin1)
