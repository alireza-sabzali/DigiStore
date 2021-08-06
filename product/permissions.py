from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return True if request.user.is_staff else False


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return True if request.user.is_staff else False
