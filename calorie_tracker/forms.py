from .models import Food
from django import forms
from django.forms.widgets import PasswordInput, TextInput
#from typing import Any
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.models import User

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name","calories","total_calories"] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter food name'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter calories'}),
            'total_calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter calories'}),
        }
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


