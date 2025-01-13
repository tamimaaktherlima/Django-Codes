from django import forms
from django.core import validators

# class contactForms(forms.Form):

    # ....... Built-in form Field .........
    # name = forms.CharField(label='User Name')
    # email = forms.EmailField(label='User Email')
    # age = forms.IntegerField(label='User Age')
    # weight = forms.FloatField(label='User Weight')
    # balance = forms.DecimalField(label='User Balance')
    # check = forms.BooleanField(label='Check Please')
    # birthday = forms.DateField()
    # appointment = forms.DateTimeField()

    # # One choice field
    # CHOICE=[('S','Small'),('M','Medium'),('L','Large')]
    # size = forms.ChoiceField(choices=CHOICE)

    # # Multiple choice field (parameter will be "List of Tuple")
    # MEAL=[('C','Cheess'),('B','Beaf'),('M','Mashroom')]
    # food_item = forms.MultipleChoiceField(choices=MEAL)


    # ...... File Upload ......
    # name = forms.CharField(label='User Name')
    # file = forms.FileField()


    # ..... Attributes and Widget
    # name = forms.CharField(label='User Name : ',help_text='Total length must be within 70 characters',required=False,widget=forms.Textarea(attrs={'id' : 'text_area','class': 'class 1 class 2','placeholder' : 'Enter your Name'}))
    # email = forms.EmailField(label='User Email')
    # age = forms.CharField(label='User Age',widget=forms.NumberInput)
    # check = forms.BooleanField(label='Check Please')
    # birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    # appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    # # One choice field
    # CHOICE=[('S','Small'),('M','Medium'),('L','Large')]
    # size = forms.ChoiceField(choices=CHOICE,widget=forms.RadioSelect)

    # # Multiple choice field (parameter will be "List of Tuple")
    # MEAL=[('C','Cheess'),('B','Beaf'),('M','Mashroom')]
    # food_item = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)

# class ValidationData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput) 

#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Enter a name within at least 10 characters')
#     #     else:
#     #         return valname
        
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('YOur email must contain .com')
#     #     else:
#     #         return valemail

#     # ...... shortCut (ekta function e sob kaj) .......
#     def clean(self):
#         cleaned_data = super().clean
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError('Enter a name within at least 10 characters')
        
#         if '.com' not in valemail:
#             raise forms.ValidationError('Your email must contain .com')
       


# .......... Built-in Validators ...........

def length_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Enter at least 10 characters')
class ValidationData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10,message='Enter a name within at maximum 10 characters')])
    # name = forms.CharField(validators=[validators.MinLengthValidator(10,message='Enter a name within at least 10 characters')])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid Email')]) 
    age = forms.IntegerField(validators=[validators.MaxValueValidator(45,message='age must be maximum 45'),validators.MinValueValidator(20,message='age must be at least 20')])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='File extension must be ended with .pdf')])

    text = forms.CharField(widget=forms.TextInput,validators=[length_check])


class Password_Validation_Project(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_confirm_pass = self.cleaned_data['Confirm_password']
        if len(val_pass) != len(val_confirm_pass):
            raise forms.ValidationError("Passowrd length doesn't match")
        elif val_pass!=val_confirm_pass:
            raise forms.ValidationError("Passowrd doesn't match")
        
        if len(val_name)<5:
            raise forms.ValidationError('Name must be at least 5 characters')