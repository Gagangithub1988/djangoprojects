from django.contrib import admin
from testApp.models import Rastaurant_Feedback
# Register your models here.
class Rastaurant_FeedbackAdmin(admin.ModelAdmin):
    list_display=['fname','lname','email','location','date','time','dine','age','foodq','services','price','experience','comment']

admin.site.register(Rastaurant_Feedback,Rastaurant_FeedbackAdmin)
