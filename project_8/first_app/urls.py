from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('password_change/',views.pass_change, name='password_change'),
    path('password_change2/',views.pass_change2, name='password_change2'),
    path('profile/',views.profile, name='profile'),
]