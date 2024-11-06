from rest_framework import serializers
from .models import Country, RoleModel, UserModel, Vacation, LikeModel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
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
        model = Vacation
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    vacationId = serializers.PrimaryKeyRelatedField(queryset=Vacation.objects.all())

    class Meta:
        model = LikeModel
        fields = ['userId', 'vacationId']

    def create(self, validated_data):
        return LikeModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.vacationId = validated_data.get('vacationId', instance.vacationId)
        instance.save()
        return instance
