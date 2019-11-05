# Viewsets
from .viewsets import HarvestViewSet

# Django rest framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', HarvestViewSet, base_name='harvest')

app_name = 'harvest'

urlpatterns = [
]

urlpatterns += router.urls
