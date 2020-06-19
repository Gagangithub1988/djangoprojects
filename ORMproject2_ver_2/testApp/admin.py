from django.contrib import admin
from testApp.models import Student,Teacher
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','address','rollno','marks']

admin.site.register(Student,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','email','address','subject','salary']

admin.site.register(Teacher,TeacherAdmin)
