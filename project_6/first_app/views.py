from django.shortcuts import render,redirect
from .import models
# Create your views here.
def home(request):
    student = models.Student.objects.all()
    return render(request, "home.html",{"data":student})

def delete_student(request,roll):
    std = models.Student.objects.get(pk = roll).delete()
    # student = models.Student.objects.all()
    # print(std)
    # return render(request, "home.html",{"data":student})
    return redirect('homepage')