from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.user_profile_page, name="user_profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("change_password/", views.change_password, name="change_password"),
]
