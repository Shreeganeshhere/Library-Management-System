from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
   path('home', views.catalog),
   path('login',include('login.urls'))
]