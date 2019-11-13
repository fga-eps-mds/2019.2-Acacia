from django.urls import path, include
from rest_framework import routers
from . import viewsets


app_name = 'harvest'

router = routers.SimpleRouter()
router.register(
    r'',
    viewsets.HarvestViewSet,
    base_name='harvest'
)

harvest_rules_router = routers.SimpleRouter()
harvest_rules_router.register(
    r'',
    viewsets.HarvestRulesViewSet,
    basename='harvest_rules'
)

urlpatterns = [
    path(
        '<int:harvest_pk>/rules/',
        include(harvest_rules_router.urls),
    ),

] + router.urls
