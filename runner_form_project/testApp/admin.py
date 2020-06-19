from django.contrib import admin
from testApp.models import Runner_Registration

# Register your models here.
class Runner_RegistrationAdmin(admin.ModelAdmin):
    list_display=['name','email','address','city','state','zip','phone','dob','gender','shirt_size','choose_race']

admin.site.register(Runner_Registration,Runner_RegistrationAdmin)
