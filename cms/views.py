from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView, GenericAPIView, CreateAPIView
)
from rest_framework.permissions import IsAuthenticated

from cms.models import *
from cms.serializers import *


class CMSMixin(GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CMS.objects.all()
    serializer_class = CMSSerializer
    lookup_field = 'id'


class CMSListCreateAPIView(ListCreateAPIView, CMSMixin): pass
class CMSDetailAPIView(RetrieveUpdateDestroyAPIView, CMSMixin): pass


class CMSTypeMixin(GenericAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'


class CMSCharMixin(CMSTypeMixin): queryset = CMSChar.objects.all(); serializer_class = CMSCharSerializer
class CMSCharCreateAPIView(CreateAPIView, CMSCharMixin): pass
class CMSCharDetailAPIView(RetrieveUpdateDestroyAPIView, CMSCharMixin): pass


class CMSTextMixin(CMSTypeMixin): queryset = CMSText.objects.all(); serializer_class = CMSTextSerializer
class CMSTextCreateCreateAPIView(CreateAPIView, CMSTextMixin): pass
class CMSTextDetailAPIView(RetrieveUpdateDestroyAPIView, CMSTextMixin): pass


class CMSImageMixin(CMSTypeMixin): queryset = CMSImage.objects.all(); serializer_class = CMSImageSerializer
class CMSImageCreateCreateAPIView(CreateAPIView, CMSImageMixin): pass
class CMSImageDetailAPIView(RetrieveUpdateDestroyAPIView, CMSImageMixin): pass


class CMSIntegerMixin(CMSTypeMixin): queryset = CMSInteger.objects.all(); serializer_class = CMSIntegerSerializer
class CMSIntegerCreateCreateAPIView(CreateAPIView, CMSIntegerMixin): pass
class CMSIntegerDetailAPIView(RetrieveUpdateDestroyAPIView, CMSIntegerMixin): pass


class CMSFloatMixin(CMSTypeMixin): queryset = CMSFloat.objects.all(); serializer_class = CMSFloatSerializer
class CMSFloatCreateCreateAPIView(CreateAPIView, CMSFloatMixin): pass
class CMSFloatDetailAPIView(RetrieveUpdateDestroyAPIView, CMSFloatMixin): pass


class CMSDatetimeMixin(CMSTypeMixin): queryset = CMSDatetime.objects.all(); serializer_class = CMSDatetimeSerializer
class CMSDatetimeCreateCreateAPIView(CreateAPIView, CMSDatetimeMixin): pass
class CMSDatetimeDetailAPIView(RetrieveUpdateDestroyAPIView, CMSDatetimeMixin): pass


class CMSBoolMixin(CMSTypeMixin): queryset = CMSBool.objects.all(); serializer_class = CMSBoolSerializer
class CMSBoolCreateCreateAPIView(CreateAPIView, CMSBoolMixin): pass
class CMSBoolDetailAPIView(RetrieveUpdateDestroyAPIView, CMSBoolMixin): pass