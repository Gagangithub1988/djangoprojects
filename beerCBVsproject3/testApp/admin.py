from django.contrib import admin
from testApp.models import Beer
# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_display=['name','taste','color']

admin.site.register(Beer,BeerAdmin)