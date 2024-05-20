from common.permissions import UserOwnerOrStaff


class ProjectPermission(UserOwnerOrStaff):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False