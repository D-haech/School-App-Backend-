from django.urls import path
from schApp import views


urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("create_school/", views.create_school, name="create-school"),
    path("get_all_school/", views.get_all_school, name="get_school"),
    path("get_all_teachers/", views.get_all_teachers, name="get_teachers"),
    path("delete_teacher/<str:uid>", views.delete_teacher, name="delete_teacher"),
    path("logout/", views.LogOut.as_view(), name="logout-user"),
    path('teacher_info/', views.teacher_info, name='teacher_info'),
    path('get_logged_in_user/', views.get_logged_in_user, name='logged_in_user'),
    path('student_info', views.student_info, name='student-info'),
    path('get_particular_school/',views.Get_particular_school.as_view(), name='get_particular_school' ),
]
