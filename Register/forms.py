from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email= forms.EmailField()
    
    class Meta:
        model = User
        fields=["email","username","password1","password2"] #order in whiich the feilds show up


