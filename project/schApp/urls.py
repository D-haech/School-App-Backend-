from django.urls import path
from schApp import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
]
