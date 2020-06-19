from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('accounts/',include('django.contrib.auth.urls')),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
                                                                name='password_change_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
                                                                name='password_change'),   
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
                                                                name='reset_password'),                                                           
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), 
                                                                name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'),
                                                                name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
                                                                name='password_reset_complete'),
]

