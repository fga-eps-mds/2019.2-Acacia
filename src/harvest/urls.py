# Viewsets
from .viewsets import HarvestViewSet

# Django rest framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', HarvestViewSet, base_name='harvest')

slashless_router = DefaultRouter(trailing_slash=False)
slashless_router.registry = router.registry[:]

app_name = 'harvest'

urlpatterns = [
]

urlpatterns += router.urls + slashless_router.urls
