from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView, ListAPIView, CreateAPIView
)

from modules.models.clubs import Club
from modules.permissions import ModulesPermission
from modules.serializers.clubs import (
    ClubSerializer, ClubGroupsSerializer,
    ClubManagersSerializer
)


class ClubMixin(GenericAPIView):
    serializer_class = ClubSerializer
    lookup_field = "slug"
    permission_classes = [ModulesPermission]


class ClubListAPIView(ListAPIView, ClubMixin):
    def get_queryset(self):
        slug = self.kwargs['module_slug']
        return Club.objects.all().filter(module__slug=slug)


class ClubCreateAPIView(CreateAPIView, ClubMixin): pass
class ClubDetailAPIView(RetrieveUpdateDestroyAPIView, ClubMixin): pass


class ClubUpdateGroupsAPIView(UpdateAPIView, ClubMixin):
    serializer_class = ClubGroupsSerializer


class ClubUpdateManagersAPIView(UpdateAPIView, ClubMixin):
    serializer_class = ClubManagersSerializer
