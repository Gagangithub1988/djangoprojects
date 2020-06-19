from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home_view),
    path('java_view/',views.java_view),
    path('my_view/',views.my_view),
    path('logout_view/',views.logout_view),
    path('accounts/',include('django.contrib.auth.urls'))
]
