from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView, ListAPIView, CreateAPIView
)

from modules.models.news import News
from modules.permissions import ModulesPermission
from modules.serializers.news import NewsSerializer


class NewsMixin(GenericAPIView):
    serializer_class = NewsSerializer
    lookup_field = "slug"
    permission_classes = [ModulesPermission]

    def get_queryset(self):
        slug = self.kwargs['module_slug']
        return News.objects.all().filter(module__slug=slug)


class NewsListAPIView(ListAPIView, NewsMixin): pass
class NewsCreateAPIView(CreateAPIView, NewsMixin): pass
class NewsDetailAPIView(RetrieveUpdateDestroyAPIView, NewsMixin): pass