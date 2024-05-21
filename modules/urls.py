from django.urls import path

from modules.views.clubs import (
    ClubDetailAPIView, ClubListAPIView,
    ClubCreateAPIView, ClubUpdateGroupsAPIView, ClubUpdateManagersAPIView
)
from modules.views.events import (
    EventDetailAPIView,
    EventUpdateOrgAPIView, EventListAPIView, EventCreateAPIView,
    EventUpdateMembersAPIView
)
from modules.views.groups import (
    GroupDetailAPIView, GroupListAPIView,
    GroupCreateAPIView, GroupUpdateTrainersAPIView, GroupUpdateMembersAPIView
)
from modules.views.news import (
    NewsDetailAPIView, NewsListAPIView,
    NewsCreateAPIView
)

urlpatterns = [
    path("events-detail/<slug:slug>/", EventDetailAPIView.as_view(), name="event-detail"),
    path("events/<slug:module_slug>", EventListAPIView.as_view(), name="event-list"),
    path("events/", EventCreateAPIView.as_view(), name="event-create"),
    path("events/<slug:slug>/change-org/", EventUpdateOrgAPIView.as_view(), name="event-change-org"),
    path("events/<slug:slug>/change-members/", EventUpdateMembersAPIView.as_view(), name="event-change-members"),

    path("news/<slug:module_slug>", NewsListAPIView.as_view(), name="news-list"),
    path("news/", NewsCreateAPIView.as_view(), name="news-create"),
    path("news-detail/<slug:slug>/", NewsDetailAPIView.as_view(), name="news-detail"),

    path("clubs-detail/<slug:slug>/", ClubDetailAPIView.as_view(), name="clubs-detail"),
    path("clubs/<slug:module_slug>", ClubListAPIView.as_view(), name="clubs-list"),
    path("clubs/", ClubCreateAPIView.as_view(), name="clubs-create"),
    path("clubs/<slug:slug>/clubs-groups/", ClubUpdateGroupsAPIView.as_view(), name="clubs-change-groups"),
    path("clubs/<slug:slug>/clubs-managers/", ClubUpdateManagersAPIView.as_view(), name="clubs-change-managers"),

    path("groups-detail/<slug:slug>/", GroupDetailAPIView.as_view(), name="groups-detail"),
    path("groups/<slug:module_slug>", GroupListAPIView.as_view(), name="groups-list"),
    path("groups/", GroupCreateAPIView.as_view(), name="groups-create"),
    path("groups/<slug:slug>/clubs-trainers/", GroupUpdateTrainersAPIView.as_view(), name="groups-change-trainers"),
    path("groups/<slug:slug>/clubs-members/", GroupUpdateMembersAPIView.as_view(), name="groups-change-members"),
]