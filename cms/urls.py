from django.urls import path

from cms.views import *

urlpatterns = [
    path("cms-list/", CMSListCreateAPIView.as_view(), name="cms-list"),
    path("cms-detail/<int:id>", CMSDetailAPIView.as_view(), name="cms-detail"),
]
