from rest_framework import serializers
from .models import ExtendedUser, LANGUAGE_CHOICES, STYLE_CHOICES


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     extended_users = serializers.HyperlinkedRelatedField(many=True, view_name='extended-user-detail', read_only=True)

#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'extended_users']


class ExtendedUserSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='extended_users_highlight', format='html')

    class Meta:
        model = ExtendedUser
        fields = ['url', 'id', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
