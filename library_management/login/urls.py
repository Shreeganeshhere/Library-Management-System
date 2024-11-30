from django.contrib import admin
from django.urls import path, include
from login import views
urlpatterns = [
    path('login/', views.login_user, name = 'login'),
    path('home',include('home.urls'), name = 'home')
]