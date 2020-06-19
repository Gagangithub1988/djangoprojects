from django.contrib import admin
from testApp.models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['cname','clocation','cceo']

admin.site.register(Company,CompanyAdmin)
