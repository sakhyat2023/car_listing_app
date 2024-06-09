from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    
    name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"class": "form-control py-2"})
    )
    
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-control py-2"})
    )
    
    body = forms.CharField(
        label="Comment", widget=forms.Textarea(attrs={"class": "form-control py-2"})
    )
    class Meta:
        model = CommentModel
        fields = ["name", "email", "body"]