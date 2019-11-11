from .viewsets import HarvestViewSet
from rest_framework.routers import DefaultRouter


app_name = 'harvest'
router = DefaultRouter()
router.register(r'', HarvestViewSet, base_name='harvest')

urlpatterns = [

] + router.urls