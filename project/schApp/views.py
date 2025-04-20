from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from schApp.serializer import CustomUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


User = get_user_model()


#This will register a user. The user should register with username and Password
@api_view(['POST'])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


#This view will login in a user with the password and username already registered
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    auth_user = authenticate(username= username, password= password)

    if auth_user is not None:
        refresh = RefreshToken.for_user(auth_user)
        context = {'access':str(refresh.access_token),'refresh':refresh.str(refresh)}
        return Response(context, status=status.HTTP_200_OK)
    else:
        return Response({'error':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)