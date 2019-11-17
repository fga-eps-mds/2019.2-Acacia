from django.urls import path, include
from .viewsets import PropertyViewSet
from rest_framework import routers


app_name = 'property'

router = routers.SimpleRouter()
router.register(r'', PropertyViewSet, basename='property')

slashless_router = routers.DefaultRouter(trailing_slash=False)
slashless_router.registry = router.registry[:]

urlpatterns = [
    path('<int:property_pk>/trees/', include('tree.urls')),
    path('<int:property_pk>/trees', include('tree.urls')),

] + router.urls + slashless_router.urls
