"""libraryproject URL Configuration

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
from libApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/', views.home1_view),
    path('home/', views.home_view),
    path('book/', views.book_view),
    path('event/', views.event_view),
    path('media/', views.media_view),
    path('contact/', views.contact_view),
    path('news/', views.news_view),
    path('photo_gallery/', views.photo_gallery_view),
    path('library/', views.library_view),
    path('testimonials/', views.testimonial_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
]