from django.shortcuts import render
from Posts.models import Post

def home(request):
    data = Post.objects.all()
    print(data)
    return render(request, 'home.html', {'data': data})