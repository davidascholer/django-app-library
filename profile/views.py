from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
# For the api view and highlight
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profile': reverse('profile-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Sets the allowable request actions with the client.
class ProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    Could be a model viewset but we don't need all of the default actions e.g. we only want to list customers in admin, not the api
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response(profile.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
        
