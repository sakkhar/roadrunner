from django import forms
from django.contrib.admin import widgets  
from django.forms import ModelForm

class AuthForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
