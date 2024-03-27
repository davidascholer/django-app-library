from rest_framework import serializers
from .models import ExtendedUser
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        User = get_user_model()
        model = User
        fields = ['url', 'email']


class ExtendedUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    # usser = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ExtendedUser
        fields = ['url','id', 'user_id', 'phone', 'birth_date', 'membership']
