from django.urls import path
from . import views

urlpatterns=[
    path('home2/',views.home_view2),
    path('login_view2/',views.login_view2),
    path('logout_view2/',views.logout_view2),
    path('register_view2/',views.register_view2),
]
