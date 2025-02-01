from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        
        # exclude menas oita bade baki sob show korbe
        # exclude = ["roll"]
        # fields = ['name','roll'] -------- (particular fields dekhar jonno)
        fields ='__all__' 
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(),
            # 'roll' : forms.PasswordInput()
        }
        help_text = {
            'name' : 'Write your full name'
        }
        error_massege = {
            'name' : {'required' : 'Your name is required'}
        }
        