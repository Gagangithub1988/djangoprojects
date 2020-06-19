"""exam_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),
    path('java_exam/', views.java_exam_view),
    path('python_exam/', views.python_exam_view),
    path('sql_exam/', views.sql_exam_view),
    path('register/', views.register_view),
    path('accounts/', include('django.contrib.auth.urls')),
]
