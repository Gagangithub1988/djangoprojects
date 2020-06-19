from django.contrib import admin
from jobApp.models import Hyderabad_jobs,Mumbai_jobs,Pune_jobs,Bangalore_jobs

# Register your models here.
class Hyderabad_jobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phnno']
class Mumbai_jobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phnno']
class Pune_jobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phnno']
class Bangalore_jobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phnno']

admin.site.register(Hyderabad_jobs,Hyderabad_jobsAdmin)
admin.site.register(Mumbai_jobs,Mumbai_jobsAdmin)
admin.site.register(Pune_jobs,Pune_jobsAdmin)
admin.site.register(Bangalore_jobs,Bangalore_jobsAdmin)
