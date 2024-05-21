from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView, ListAPIView, CreateAPIView
)

from modules.models.groups import Group
from modules.permissions import ModulesPermission
from modules.serializers.groups import (
    GroupTrainersSerializer,
    GroupMembersSerializer, GroupSerializer
)


class GroupMixin(GenericAPIView):
    serializer_class = GroupSerializer
    lookup_field = "slug"
    permission_classes = [ModulesPermission]


class GroupListAPIView(ListAPIView, GroupMixin):
    def get_queryset(self):
        slug = self.kwargs['module_slug']
        return Group.objects.all().filter(module__slug=slug)


class GroupCreateAPIView(CreateAPIView, GroupMixin): pass
class GroupDetailAPIView(RetrieveUpdateDestroyAPIView, GroupMixin): pass


class GroupUpdateTrainersAPIView(UpdateAPIView, GroupMixin):
    serializer_class = GroupTrainersSerializer


class GroupUpdateMembersAPIView(UpdateAPIView, GroupMixin):
    serializer_class = GroupMembersSerializer
