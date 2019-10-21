from django.urls import path, include
from .viewsets import PropertyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PropertyViewSet, base_name='property')

app_name = 'property'

urlpatterns = [
]

urlpatterns += router.urls