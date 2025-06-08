from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from schApp.serializer import CustomUserSerializer, SchoolSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .models import CustomUser, School
from .permissions import IsSchoolAdmin, IsTeacher, IsStudent
from rest_framework.permissions import IsAuthenticated


# Create your views here.


User = get_user_model()


# This will register a user. The user should register with username and Password
@api_view(["POST"])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# This view will login a user with the password and username already registered
@api_view(["GET"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    auth_user = authenticate(username=username, password=password)

    if auth_user is not None:
        refresh = RefreshToken.for_user(auth_user)
        context = {"access": str(refresh.access_token), "refresh": str(refresh)}
        return Response(context, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


# creates a school account
@api_view(["POST"])
def create_school(request):
    serializer = SchoolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# This is used to get the entire school object. the entire details of a school
@api_view(["GET"])
def get_school(request):
    school = School.objects.all()
    serialize = SchoolSerializer(school, many=True)
    return Response(serialize.data, status=status.HTTP_200_OK)


# get all the list of teachers in a school
@api_view(["GET"])
@permission_classes([IsSchoolAdmin])
def get_all_teachers(request):
    teachers = CustomUser.objects.filter(school=request.user.school)

    if not teachers.exists():
        return Response({"message": "You do not have teachers assigned to your school"})
    else:
        serializer = CustomUserSerializer(teachers, many=True)
        return Response(serializer.data)


# This is used by the school-admin to delete a teacher
@api_view(["DELETE"])
@permission_classes([IsSchoolAdmin])
def delete_teacher(request, uid):
    teacher = CustomUser.objects.get(pk=uid)
    teacher.delete()
    return Response({"message": "teacher deleted"}, status=status.HTTP_200_OK)

#This is used to logout
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response ({"message": "Successfully logged out"}, status= status.HTTP_205_RESET_CONTENT)
    except KeyError:
        return Response({"error":"Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
    except TokenError:
        return Response({"error":"Token is invalid or expired"}, status=status.HTTP_400_BAD_REQUEST)

#This is used to get the logged in teacher's  profile information
@api_view(["GET"])
@permission_classes([IsTeacher])
def teacher_info(request):
    teacher = request.user
    serializer = CustomUserSerializer(teacher)
    return Response(serializer.data, status=status.HTTP_200_OK)

#This is used to get the logged in students' profile information 
@api_view(["GET"])
@permission_classes([IsStudent])
def student_info(request):
    student = request.user
    serialize = CustomUserSerializer(student)
    return Response(serialize.data, status=status.HTTP_200_OK)
