from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from drf_yasg import openapi


User = get_user_model()

register_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='User created successfully'),
        'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token'),
    }
)

login_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token'),
    }
)

def login_redirect(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'role') and request.user.role == 'admin':
            return redirect('/admin/')
        return redirect('base_page')
    return redirect('account_login')


@login_required
def base_page(request):
    return render(request, 'base_page.html')

@swagger_auto_schema(
    method='post',
    request_body=RegisterSerializer,
    responses={
        status.HTTP_201_CREATED: register_response_schema,
        status.HTTP_400_BAD_REQUEST: 'Bad request'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'message': 'User created successfully', 'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=LoginSerializer,
    responses={
        status.HTTP_201_CREATED: login_response_schema,
        status.HTTP_400_BAD_REQUEST: 'Invalid credentials'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@swagger_auto_schema(
    method='post',
    responses={
        200: 'Logged out successfully',
        401: 'User not authenticated'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def api_logout(request):
    if request.user.is_authenticated:
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
