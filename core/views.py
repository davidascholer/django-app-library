from .models import User
from .serializers import UserSerializer, UserDeleteSerializer
# For the api view and highlight
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from .permissions import IsAdminOrOwner
from rest_framework import status
from rest_framework.decorators import action
from djoser import utils
from djoser.conf import settings

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#     })

# set for router urls
class UserViewSet(DjoserUserViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    print("DEBUG user viewset")
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrOwner]

    class Meta:
        model = User
        fields = ['id', 'email']

    def destroy(self, request, *args, **kwargs):
        print("DEBUG user destroy")
        instance = self.get_object()
        
        if instance == request.user:
            utils.logout_user(self.request)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
