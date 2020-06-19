from django.contrib import admin
from fakeApp.models import School
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display=['name','rollno','addr']

admin.site.register(School,SchoolAdmin)
