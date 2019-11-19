from django.contrib import admin
from django.urls import path, include
from .helpers import list_all_endpoints
from harvest.viewsets import WeekHarvests


urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    path('properties/', include('property.urls')),

    # TODO: We could create a dynamic route that
    # creates different queries according to the
    # parameter passed in the url.

    # path(
    #     'harvests/<int:timedelta>/',
    #     WeekHarvests.as_view({'get': 'list'})
    # ),

    path(
        'harvests/',
        WeekHarvests.as_view({'get': 'list'}),
        name='weekly_harvests'
    ),
]

urlpatterns = list_all_endpoints(urlpatterns)
