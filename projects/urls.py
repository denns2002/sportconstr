from django.urls import path

from .views import *


urlpatterns = [
    path("project-list/", ProjectListCreateAPIView.as_view(), name="project-list"),
    path("project-detail/<slug:slug>", ProjectDetailAPIView.as_view(), name="project-detail"),

    path("sample-list/", SampleListCreateAPIView.as_view(), name="sample-list"),
    path("sample-detail/<slug:slug>", SampleDetailAPIView.as_view(), name="sample-detail"),

    path("module-list/<slug:project_slug>", ModuleListAPIView.as_view(), name="module-list"),
    path("module-create/", ModuleCreateAPIView.as_view(), name="module-create"),
    path("module-detail/<slug:slug>", ModuleDetailAPIView.as_view(), name="module-detail"),

    path("style-list/", StyleListCreateAPIView.as_view(), name="style-list"),
    path("style-detail/<slug:slug>", StyleDetailAPIView.as_view(), name="style-detail"),

    path("typography-list/", TypographyListCreateAPIView.as_view(), name="typography-list"),
    path("typography-detail/<slug:slug>", TypographyDetailAPIView.as_view(), name="typography-detail"),

    path("palette-list/", PaletteListCreateAPIView.as_view(), name="palette-list"),
    path("palette-detail/<slug:slug>", PaletteDetailAPIView.as_view(), name="palette-detail"),
]
