from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        # jodi models.py er sob gulo features use korte chai
        fields = '__all__'
        # specific kichu features use korte chaile
        # fields = ['name','bio']
        # 'bio' bade onno sob use korbo
        # exclude = ['bio']