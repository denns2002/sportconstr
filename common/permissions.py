from rest_framework import permissions


class UserOwnerOrStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True
        
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True

        if obj == request.user:
            return True

        try:
            if obj.user == request.user:
                return True
        except Exception:
            pass

        return False
