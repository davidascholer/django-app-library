from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsAdminOrReadOnly, ViewCustomerHistoryPermission
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions
# from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
# from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'userprofile': reverse('user-profile-list', request=request, format=format)
    })

"""
Instead of disallowing access via custom Mixins, we do it through permissions.
e.g.

instead of: 
class ProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        ...

we use:
class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        ...
"""
# Sets the allowable request actions with the client.
class UserProfileViewSet(ModelViewSet):
    """
    Could be a model viewset but we don't need all of the default actions e.g. we only want to list customers in admin, not the api
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]

    # for the highlight render options
    @action(detail=True)
    def highlight(self, request, *args, **kwargs):
        userprofile = self.get_object()
        return Response(userprofile.highlighted)
    
    # detail=False means the action is availeble on the list view "api/userprofile/"
    # detail=True means the action is available on the detail view "api/userprofile/<id>/"
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        # if user is logged in, this will be a user object
        # if user is not logged in, it will be an instance of 'AnonymousUser'
        # if no userprofile exists, one will be created
        userprofile = UserProfile.objects.get(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = UserProfileSerializer(userprofile)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserProfileSerializer(userprofile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    # the action is availeble on the endpoint "api/userprofile/<id>/history/"
    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
    def history(self, request, pk):
        return Response('ok')
    
    def destroy(self, request, *args, **kwargs):
        print('kwargs from userprofile views',kwargs)
        return Response({'error': 'User cannot be deleted because it is associated with user profile.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        # if User.objects.filter(product_id=kwargs['pk']).count() > 0:
        #     return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        # return super().destroy(request, *args, **kwargs)

        
