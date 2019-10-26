from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tree.viewsets import TreeViewSet


router = routers.DefaultRouter()
router.register(r'tree', TreeViewSet)


urlpatterns = [
    path('', include(router.urls)), 

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]


