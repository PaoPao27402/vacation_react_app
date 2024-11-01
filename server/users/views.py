# users/views.py
from rest_framework import generics, status # type: ignore
from rest_framework.permissions import AllowAny # type: ignore
from rest_framework.response import Response # type: ignore
from .models import User
from .serializers import UserSerializer, LoginSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

from django.contrib.auth import authenticate

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # Authenticate using email as username
        user = authenticate(request=request, username=email, password=password)

        if user is None:
            return Response({"non_field_errors": ["Invalid email or password."]}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

