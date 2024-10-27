# users/views.py
from rest_framework import generics # type: ignore
from rest_framework.permissions import AllowAny # type: ignore
from .models import User
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
