from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("THis is my firts_App about page")
def courese(request):
    return HttpResponse("THis is my first_App courses page")
def home(request):
    return HttpResponse("THis is my first_App home page")

