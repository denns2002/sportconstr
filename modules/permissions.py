from rest_framework import permissions


class ModulesPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True

        try:
            if obj.project.user == request.user:
                return True
        except Exception:
            pass

        try:
            if obj.project.staff.get(id=request.user.id):
                return True
        except Exception:
            pass

        try:
            if obj.module.project.user == request.user:
                return True
        except Exception:
            pass

        return False


