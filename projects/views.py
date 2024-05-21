from django.db.models import Q
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView, GenericAPIView, CreateAPIView, ListAPIView
)
from rest_framework.permissions import IsAdminUser

from modules.permissions import ModulesPermission
from projects.permissions import ProjectPermission
from projects.serializers import *


class ProjectMixin(GenericAPIView):
    permission_classes = [ProjectPermission]
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Project.objects.filter(Q(staff=self.request.user) | Q(user=self.request.user))

        return queryset


class ProjectListCreateAPIView(ListCreateAPIView, ProjectMixin): pass
class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView, ProjectMixin): pass


class ModulesMixin(GenericAPIView):
    permission_classes = [ModulesPermission]
    lookup_field = 'slug'


class SampleMixin(ModulesMixin):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleListCreateAPIView(ListCreateAPIView, SampleMixin): pass
class SampleDetailAPIView(RetrieveUpdateDestroyAPIView, SampleMixin): pass


class ModuleMixin(ModulesMixin):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleListAPIView(ListAPIView, ModuleMixin):
    def get_queryset(self):
        project_slug = self.kwargs['project_slug']
        return self.queryset.filter(project__slug=project_slug)


class ModuleCreateAPIView(CreateAPIView, ModuleMixin): pass
class ModuleDetailAPIView(RetrieveUpdateDestroyAPIView, ModuleMixin): pass


class StyleMixin(ModulesMixin):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class StyleListCreateAPIView(ListCreateAPIView, StyleMixin): pass
class StyleDetailAPIView(RetrieveUpdateDestroyAPIView, StyleMixin): pass


class TypographyMixin(ModulesMixin):
    queryset = Typography.objects.all()
    serializer_class = TypographySerializer


class TypographyListCreateAPIView(ListCreateAPIView, TypographyMixin): pass
class TypographyDetailAPIView(RetrieveUpdateDestroyAPIView, TypographyMixin): pass


class PaletteMixin(ModulesMixin):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer


class PaletteListCreateAPIView(ListCreateAPIView, PaletteMixin): pass
class PaletteDetailAPIView(RetrieveUpdateDestroyAPIView, PaletteMixin): pass




