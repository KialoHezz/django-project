from django import forms 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # RegisterForm is register in db of user
    class Meta:
        model = User
        # to appear
        fields = ["username", "email", "password"]
