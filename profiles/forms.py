from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        label="User Name", widget=forms.TextInput(attrs={"class": "form-control py-2"})
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control py-2"})
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class ChangeUserPasswordForm(PasswordChangeForm):

    old_password = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(attrs={"class": "form-control py-2"}),
    )

    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"class": "form-control py-2"}),
    )

    new_password2 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"class": "form-control py-2"}),
    )

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
