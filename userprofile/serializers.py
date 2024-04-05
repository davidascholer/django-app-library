from rest_framework import serializers
from .models import UserProfile
from .signals import user_created


# Sets which tables from a model to take actions on at "profiles/userprofile/me/"
class UserProfileSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField(read_only=True)
    # user = serializers.ReadOnlyField(source='user.email')

    # Show which fields show up at "profiles/userprofile/me/"
    class Meta:
        model = UserProfile
        fields = ['id', 'user_id', 'phone', 'birth_date', 'membership']

