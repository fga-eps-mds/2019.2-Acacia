from django.contrib import admin
from django.urls import path, include
from .helpers import list_all_endpoints
from harvest.viewsets import WeekHarvests, MonthlyHarvests


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('harvests/', include('harvest.urls')),
    path('harvests', include('harvest.urls')),
    path('properties/', include('property.urls')),
    path('properties', include('property.urls')),
    path(
        'weekly_harvests/',
        WeekHarvests.as_view({'get': 'list'}),
        name='weekly_harvests'
    ),

    path(
        'monthly_harvest/<int:year>/<int:month>/',
        MonthlyHarvests.as_view({'get': 'list'}),
        name='monthly_harvest'
    ),
]

urlpatterns = list_all_endpoints(urlpatterns)
