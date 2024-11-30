from django.contrib import admin
from django.urls import path, include
from console import views

app_name = 'console'
urlpatterns = [
    path('add_books/', views.addbooks, name = 'addbooks'),
]
