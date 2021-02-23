from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    year=forms.CharField()
    class Meta:
        model=User
        fields=['username','email','year','password1','password2']