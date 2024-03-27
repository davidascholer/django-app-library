from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
# from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class UserSerializer(serializers.ModelSerializer):
# class UserSerializer(BaseUserSerializer):
    
    class Meta:
        User = get_user_model()
        model = User
        fields = ['url', 'email', 'id']


# Sets which tables from a model to take actions on
class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    # usser = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ['url','id', 'user_id', 'phone', 'birth_date', 'membership']
