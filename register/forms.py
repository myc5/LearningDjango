from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    
    class Meta:
        model = User # change the User form when we save
        fields = ["username", "email", "password1", "password2"] # order of fields; the EmailField wouldn't show up if not defined here, password1/2, username are from UserCreationForm