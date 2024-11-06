from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = CountryModel
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoleModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = "__all__"

class VacationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacationModel
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), source='userID')
    vacation = serializers.PrimaryKeyRelatedField(queryset=VacationModel.objects.all(), source='vacationId')

    class Meta:
        model = LikeModel
        fields = ['user', 'vacation']

    def create(self, validated_data):
        return LikeModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userID = validated_data.get('userID', instance.userID)
        instance.vacationId = validated_data.get('vacationId', instance.vacationId)
        instance.save()
        return instance