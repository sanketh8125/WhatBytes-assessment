"""
URL configuration for WhatBytes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('login/', views.login_view, name='login'),
   path('signup', views.signup, name='signup'),
   path('profile', views.profile, name='profile'),
   path('forgot-password', views.forgotPassword, name='forgotPassword'),
   path('change-password', views.changePassword, name='changePassword'),
   path('dashboard', views.dashboard, name='dashboard'),
   path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
   path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
   path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
