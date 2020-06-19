from django.contrib import admin
from testApp.models import MovieInfo
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['date','moviename','hero','heroine','rating']

admin.site.register(MovieInfo,MovieAdmin)
