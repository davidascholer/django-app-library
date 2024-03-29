from rest_framework import permissions

# Example of custom permission
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


# Example of overriding the default permissions
class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

# Example of custom model permissions
class ViewCustomerHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # from UserProfile model
        return request.user.has_perm('userprofile.view_history')