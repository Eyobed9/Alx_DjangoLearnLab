from rest_framework.permissions import BasePermission

class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff