from django.shortcuts import render
from django import forms
# from .form import contactForms,ValidationData
from .form import ValidationData,Password_Validation_Project
 
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('userName')
        email = request.POST.get('userEmail')
        select = request.POST.get('select')
        return render(request, 'about.html',{'name':name,'email':email,'select':select})
    else:
       return render(request, 'about.html')

def form(request):
    return render(request, 'form.html')

# def DjangoForm(request):
#     # form = contactForms()
#     # print direct html code
#     # print(form)

#     # print value
#     if request.method=='POST':
#         form = contactForms(request.POST, request.FILES)
#         if form.is_valid():

#             # upload file
#             # file = form.cleaned_data['file']
#             # with open('./first_app/upload/' + file.name, 'wb+') as destination:
#             #     for chunk in file.chunks():
#             #         destination.write(chunk)
#             # print(form.cleaned_data)

#             return render(request, 'django_form.html', {'form': form})
#     else:
#         form =contactForms()
#         return render(request, 'django_form.html', {'form': form})
    

def validation_Data_form(request):
    if request.method=='POST':
        form = ValidationData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form =ValidationData()
    return render(request, 'django_form.html', {'form': form})

def password_validation(request):
    if request.method=='POST':
        form = Password_Validation_Project(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form =Password_Validation_Project()
    return render(request, 'django_form.html', {'form': form})