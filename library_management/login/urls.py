from django.contrib import admin
from django.urls import path, include
from login import views

app_name = 'login'
urlpatterns = [
    path('login/', views.login_user, name = 'login'),
    path('',include('home.urls'), name = 'home')
]