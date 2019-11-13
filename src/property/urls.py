from django.urls import path, include
from .viewsets import PropertyViewSet
from rest_framework import routers


app_name = 'property'

router = routers.SimpleRouter()
router.register(r'', PropertyViewSet, basename='property')

urlpatterns = [
    path(
        '<int:property_pk>/trees/',
        include('tree.urls')
    ),

    path(
        '<int:property_pk>/harvests/',
        include('harvest.urls')
    ),

] + router.urls
