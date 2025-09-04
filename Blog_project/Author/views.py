from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def add_authors(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_authors')
    else:
        author_form = forms.AuthorForm()
    return render(request, 'add_authors.html',{'form': author_form})