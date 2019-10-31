from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tree.viewsets import TreeViewSet

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'tree', TreeViewSet)
# router.register(r'tree', TreeViewSet, base_name='Tree')

from .helpers import list_all_endpoints

urlpatterns = [
    path('', include(router.urls)), 
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('properties/', include('property.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = list_all_endpoints(urlpatterns)
