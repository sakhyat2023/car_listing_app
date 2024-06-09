from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="User Name",widget=forms.TextInput(attrs={"class": "form-control py-2"}))
    
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control py-2"}))
    
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class": "form-control py-2"}))
    
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class": "form-control py-2"}))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]