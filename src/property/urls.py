from django.urls import path, include
from .viewsets import PropertyViewSet
from rest_framework.routers import DefaultRouter


app_name = 'property'

urlpatterns = [
    path(
        '',
        PropertyViewSet.as_view({
            'get': 'list',
            'post':'create'
        })
    ),

    path('<int:pk>/trees/', include('tree.urls')),

    path(
        '<int:pk>/',
        PropertyViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
        })
    ),
]
