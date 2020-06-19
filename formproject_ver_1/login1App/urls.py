from django.urls import path
from login1App import views
urlpatterns=[
    path('register_view1/',views.register_view1),
    path('login_view1/',views.login_view1),
    path('logout_view1/',views.logout_view1),
    path('home1/',views.home_view1),
]
