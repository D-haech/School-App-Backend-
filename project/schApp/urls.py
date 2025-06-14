from django.urls import path
from schApp import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("create_school/", views.create_school, name="create-school"),
    path("get_school/", views.get_school, name="get_school"),
    path("get_all_teachers/", views.get_all_teachers, name="get_teachers"),
    path("delete_teacher/<str:uid>", views.delete_teacher, name="delete_teacher"),
    path("logout/", views.logout_user, name="logout-user"),
    path('teacher_info/', views.teacher_info, name='teacher_info'),
    path('get_logged_in_user/', views.get_logged_in_user, name='logged_in_user'),
]
