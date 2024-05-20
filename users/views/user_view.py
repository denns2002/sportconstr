from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from common.permissions import UserOwnerOrStaff
from users.serializers.user_serializer import UserSerializer


class UserMixin(GenericAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView, UserMixin):
    permission_classes = [IsAdminUser]


class UserDetailAPIView(RetrieveUpdateDestroyAPIView, UserMixin):
    permission_classes = [UserOwnerOrStaff]
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
