from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('properties/', include('property.urls')),
]

from .helpers import list_all_endpoints
urlpatterns = list_all_endpoints(urlpatterns)

