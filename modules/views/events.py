from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView, ListAPIView, CreateAPIView
)

from modules.models.events import Event
from modules.permissions import ModulesPermission
from modules.serializers.events import (
    EventSerializer,
    EventOrganizersSerializer, EventUpdatersSerializer
)


class EventMixin(GenericAPIView):
    serializer_class = EventSerializer
    lookup_field = "slug"
    permission_classes = [ModulesPermission]


class EventListAPIView(ListAPIView, EventMixin):
    def get_queryset(self):
        slug = self.kwargs['module_slug']
        return Event.objects.all().filter(module__slug=slug)


class EventCreateAPIView(CreateAPIView, EventMixin): pass
class EventDetailAPIView(RetrieveUpdateDestroyAPIView, EventMixin): pass


class EventUpdateOrgAPIView(UpdateAPIView, EventMixin):
    """
    Add organizers to events.

    - Gives full access to the event's CRUD.
    - The specified profiles will be in the contacts of the event.
    """

    serializer_class = EventOrganizersSerializer


class EventUpdateMembersAPIView(UpdateAPIView, EventMixin):
    serializer_class = EventUpdatersSerializer