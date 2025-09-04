from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
# def add_authors(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_authors')
#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_authors.html',{'form': author_form})

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return redirect(request, 'register.html', {'form' : register_form, 'type' :'Register'}) 

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password =user_pass)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return redirect('register')
    else:
        form = AuthenticationForm()
        return redirect(request, 'register.html', {'form' : form, 'type' :'Login'})        
    