from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.add_profiles, name='add_profiles')
]