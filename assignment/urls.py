from ast import Assign
from django.contrib import admin
from django.urls import path, include
from assignment import views

urlpatterns = [
    path('', views.index, name='home')
]
