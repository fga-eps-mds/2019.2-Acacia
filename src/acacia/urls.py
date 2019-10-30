from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from .helpers import list_all_endpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('properties/', include('property.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
    
urlpatterns = list_all_endpoints(urlpatterns)
