from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import VacationModel, LikeModel, UserModel, CountryModel
from .serializers import VacationSerializer, LikeSerializer, UserSerializer, CountrySerializer

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

    User = get_user_model()
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.check_password(password):
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    token = AccessToken.for_user(user)
    return Response({
        'token': str(token),
        'user': {
            'email': user.email,
            'firstName': user.first_name,
            'lastName': user.last_name,
        }
    })
