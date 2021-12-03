from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),
    path('',views.index, name='index'),
]