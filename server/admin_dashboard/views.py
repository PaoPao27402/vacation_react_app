from rest_framework_simplejwt.tokens import AccessToken
from django.utils import timezone
from itertools import count
from admin_dashboard import models
from django.db.models import Count, Q
from .models import VacationModel, LikeModel, UserModel, CountryModel
from .serializers import VacationSerializer, LikeSerializer, UserSerializer, CountrySerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from .models import UserModel  


@api_view(['GET'])
def get_vacations(request):
    vacations = VacationModel.objects.all()
    serializer = VacationSerializer(vacations, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_likes(request):
    likes = LikeModel.objects.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_users(request):
    users = UserModel.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_countries(request):
    countries = CountryModel.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # Print received credentials for debugging
    print(f"Received email: {email}, password: {password}")

    User = get_user_model()  # Get the user model
    try:
        user = User.objects.get(email=email)  # Retrieve user by email
    except User.DoesNotExist:
        print("User does not exist.")
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # Verify the password
    if not user.check_password(password):  # Compare the hashed password
        print("Incorrect password.")
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    # If user is authenticated, generate a JWT token
    token = AccessToken.for_user(user)
    return Response({
        'token': str(token),
        'user': {
            # 'userId': user.userId,
            'email': user.email,
            'firstName': user.first_name,
            'lastName': user.last_name,
            # 'roleId': user.roleId
        }
    })
