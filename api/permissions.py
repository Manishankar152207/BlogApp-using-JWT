from rest_framework import permissions

class ExcludeAuthenticationForGetMethod(permissions.BasePermission):
    """Returns the permission based on the type of action"""
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
