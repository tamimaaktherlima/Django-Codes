

from django.urls import path
from .import views
urlpatterns = [
    path("courses/", views.courese),
    path("about/", views.about),
    path("", views.home)
]