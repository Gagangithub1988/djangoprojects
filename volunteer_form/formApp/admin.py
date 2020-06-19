from django.contrib import admin
from formApp.models import Volunteer

# Register your models here.
class VolunteerAdmin(admin.ModelAdmin):
    list_display=['name','email','phoneno','password','course','date','agreement']

admin.site.register(Volunteer,VolunteerAdmin)
