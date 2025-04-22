from django.urls import path
from schApp import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path('create_school/', views.create_school, name='create-school'),
    path('get_school/', views.get_school, name='get_school')
    
]
