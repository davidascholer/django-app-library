from rest_framework import permissions

class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Return read only if the request is safe
        if request.method in permissions.SAFE_METHODS:
            return True
        # Return true if the user is an admin or matches the object user
        return bool(request.user.is_staff or (obj == request.user))
    
class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Return true if the user is an admin or matches the object user
        return bool(request.user.is_staff or (obj == request.user))