"""CBVsproject2 URL Configuration

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
from django.urls import path
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_view/', views.list_view.as_view(),name='companies'),
    path('detail_view/<pk>', views.detail_view.as_view(),name='detail'),
    path('create_view/', views.create_view.as_view()),
    path('update_view/<pk>', views.update_view.as_view()),
    path('delete_view/<pk>', views.delete_view.as_view()),
]
