from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="User Name",widget=forms.TextInput(attrs={"class": "form-control py-2"}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class": "form-control py-2"}))
    
    class Meta:
        model = User
        fields = ["username", "password"]