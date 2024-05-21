from django.urls import path

from cms.views import *

urlpatterns = [
    path("cms-list/", CMSListCreateAPIView.as_view(), name="cms-list"),
    path("cms-detail/<slug:slug>", CMSDetailAPIView.as_view(), name="cms-detail"),

    path("cms-char-create/", CMSCharCreateAPIView.as_view(), name="cms-char-create"),
    path("cms-char/<slug:slug>", CMSCharDetailAPIView.as_view(), name="cms-char-detail"),

    path("cms-text-create/", CMSTextCreateCreateAPIView.as_view(), name="cms-text-create"),
    path("cms-text/<slug:slug>", CMSTextDetailAPIView.as_view(),name="cms-text-detail"),

    path("cms-image-create/", CMSImageCreateCreateAPIView.as_view(), name="cms-image-create"),
    path("cms-image/<slug:slug>", CMSImageDetailAPIView.as_view(), name="cms-image-detail"),

    path("cms-integer-create/", CMSIntegerCreateCreateAPIView.as_view(), name="cms-integer-create"),
    path("cms-integer/<slug:slug>", CMSIntegerDetailAPIView.as_view(), name="cms-integer-detail"),

    path("cms-float-create/", CMSFloatCreateCreateAPIView.as_view(), name="cms-float-create"),
    path("cms-float/<slug:slug>", CMSFloatDetailAPIView.as_view(), name="cms-float-detail"),

    path("cms-datetime-create/", CMSDatetimeCreateCreateAPIView.as_view(), name="cms-datetime-create"),
    path("cms-datetime/<slug:slug>", CMSDatetimeDetailAPIView.as_view(), name="cms-datetime-detail"),

    path("cms-bool-create/", CMSBoolCreateCreateAPIView.as_view(), name="cms-bool-create"),
    path("cms-bool/<slug:slug>", CMSBoolDetailAPIView.as_view(), name="cms-bool-detail"),
]
