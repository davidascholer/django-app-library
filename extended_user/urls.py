from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'extended-users', views.ExtendedUserViewSet, basename='extended-user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]