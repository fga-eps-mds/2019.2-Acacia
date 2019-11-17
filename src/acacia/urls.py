from django.contrib import admin
from django.urls import path, include
from .helpers import list_all_endpoints


urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    path('harvests/', include('harvest.urls')),
    path('harvests', include('harvest.urls')),

    path('properties/', include('property.urls')),
    path('properties', include('property.urls')),
]


urlpatterns = list_all_endpoints(urlpatterns)
