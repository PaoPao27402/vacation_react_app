# vacations/serializers.py
from rest_framework import serializers # type: ignore
from .models import Vacation, User

class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_admin']