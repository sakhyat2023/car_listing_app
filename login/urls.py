from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.LogoutViewClass.as_view(), name="logout")
]
