from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginUserForm

# Create your views here.


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"

    def get_success_url(self) -> str:
        return reverse_lazy("user_profile")


class LogoutViewClass(LogoutView):

    def get_success_url(self) -> str:
        return reverse_lazy("login")
