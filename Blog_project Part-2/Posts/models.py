from django.db import models
from Categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # ekta post multiple category er moddhe thakte pare abr ekta category multiple post er moddhe thakte pare
    category = models.ManyToManyField(Category)

    # Author delete korar sathe sathe tar sob Post o delete hoye jabe.
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return {self.title}