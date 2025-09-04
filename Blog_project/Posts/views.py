from django.shortcuts import render,redirect
from .import models
from .import forms
# Create your views here.
def add_posts(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_posts')
    else:
        post_form = forms.PostForm()
    return render(request, 'add_posts.html',{'form': post_form})

def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    # print(post.title)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render(request, 'add_posts.html',{'form': post_form})

def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')