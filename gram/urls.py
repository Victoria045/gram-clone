from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('account/', include('django.contrib.auth.urls')),
    path('index/',views.index, name='index'),
]