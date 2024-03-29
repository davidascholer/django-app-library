from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from rest_framework import serializers
from rest_framework.settings import api_settings


# Sets which tables to display to the client for literal endpoints as well as djoser auth endpoints
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password']

    # Override to set username to email
    def validate(self, attrs):
        email = attrs.get("email")
        attrs = {"username":email,**attrs}
        return super().validate(attrs)
        
# Sets which tables to display to the client for literal endpoints as well as djoser auth endpoints
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['id', 'email']

