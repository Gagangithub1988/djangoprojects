from django.contrib import admin
from testApp.models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name']

admin.site.register(Register,RegisterAdmin)
