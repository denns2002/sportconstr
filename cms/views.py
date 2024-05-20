from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView, GenericAPIView
)
from rest_framework.permissions import IsAuthenticated

from cms.models import CMS
from cms.serializers import CMSSerializer


class CMSMixin(GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CMS.objects.all()
    serializer_class = CMSSerializer
    lookup_field = 'id'


class CMSListCreateAPIView(ListCreateAPIView, CMSMixin):
    pass


class CMSDetailAPIView(RetrieveUpdateDestroyAPIView, CMSMixin):
    pass

