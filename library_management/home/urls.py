from django.contrib import admin
from django.urls import path, include
from home import views

app_name = 'home'
urlpatterns = [
   path('', views.home,name='home'),
   path('login/',include('login.urls'),name='login'),
   path('addbooks/',include('console.urls'),name='addbooks'),
]