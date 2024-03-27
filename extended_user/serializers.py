from rest_framework import serializers
from .models import ExtendedUser


class ExtendedUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    # usser = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = ExtendedUser
        fields = ['url','id', 'user_id', 'phone', 'birth_date', 'membership']
