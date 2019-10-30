from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .helpers import list_all_endpoints
from rest_framework import routers
from upload.viewsets import PictureViewSet

router = routers.DefaultRouter()
router.register(r'picture', PictureViewSet)


urlpatterns = [
    path('', include(router.urls)), 

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('properties/', include('property.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT
    
urlpatterns = list_all_endpoints(urlpatterns)
