from django.db import models
from Author.models import Author

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    author = models.OneToOneField(Author, on_delete= models.CASCADE,default=None)

    def __str__(self):
        return self.name
        # return self.author.name