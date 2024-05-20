from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView, GenericAPIView
)
from rest_framework.permissions import IsAdminUser

from projects.permissions import ProjectPermission
from projects.serializers import *


class ProjectMixin(GenericAPIView):
    permission_classes = [ProjectPermission]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'


class ProjectListCreateAPIView(ListCreateAPIView, ProjectMixin): pass
class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView, ProjectMixin): pass


class AdminMixin(GenericAPIView):
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'


class SampleMixin(AdminMixin):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleListCreateAPIView(ListCreateAPIView, SampleMixin): pass
class SampleDetailAPIView(RetrieveUpdateDestroyAPIView, SampleMixin): pass


class ModuleMixin(AdminMixin):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleListCreateAPIView(ListCreateAPIView, ModuleMixin): pass
class ModuleDetailAPIView(RetrieveUpdateDestroyAPIView, ModuleMixin): pass


class StyleMixin(AdminMixin):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class StyleListCreateAPIView(ListCreateAPIView, StyleMixin): pass
class StyleDetailAPIView(RetrieveUpdateDestroyAPIView, StyleMixin): pass


class TypographyMixin(AdminMixin):
    queryset = Typography.objects.all()
    serializer_class = TypographySerializer


class TypographyListCreateAPIView(ListCreateAPIView, TypographyMixin): pass
class TypographyDetailAPIView(RetrieveUpdateDestroyAPIView, TypographyMixin): pass


class PaletteMixin(AdminMixin):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer


class PaletteListCreateAPIView(ListCreateAPIView, PaletteMixin): pass
class PaletteDetailAPIView(RetrieveUpdateDestroyAPIView, PaletteMixin): pass




