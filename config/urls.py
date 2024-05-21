from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="SPORT",
      default_version='v0.1',
      description="SWAGGER API",
      contact=openapi.Contact(email="@denisisrafilov"),
   ),
   public=False,  # show endpoint only with permissions
   permission_classes=(permissions.AllowAny,),  # указать свой
)

urlpatterns = [
   path("admin/", admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path("users/", include("users.urls")),
   path("cms/", include("cms.urls")),
   path("projects/", include("projects.urls")),
   path("modules/", include("modules.urls")),
]
