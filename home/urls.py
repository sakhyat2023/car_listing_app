from django.urls import path
from .import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("<slug:name>", views.car_details_page, name="car_details"),
    path("add_to_cart/<slug:name>/", views.add_to_cart, name="add_to_cart"),
    path("brand/<slug:brand_slug>/", views.home_page, name="car_list"),
]
