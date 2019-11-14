from django.contrib import admin
from django.urls import path, include
from .helpers import list_all_endpoints
from harvest.viewsets import WeekHarvests


urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    path('properties/', include('property.urls')),

    path(
        'harvests/',
        WeekHarvests.as_view({'get': 'list'})
    ),
]

urlpatterns = list_all_endpoints(urlpatterns)
