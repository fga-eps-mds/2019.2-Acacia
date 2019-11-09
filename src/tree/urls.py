from .viewsets import TreeViewSet, HarvestMonthViewSet
from django.urls import path, include
from rest_framework import routers


app_name = 'tree'

tree_router = routers.SimpleRouter()
tree_router.register(r'', TreeViewSet, basename='tree')

harvest_month_router = routers.SimpleRouter()
harvest_month_router.register(
    r'',
    HarvestMonthViewSet,
    basename='harvest_months'
)

urlpatterns = [
    path(
        '<int:tree_pk>/harvest_months/',
        include(harvest_month_router.urls),
    ),

] + tree_router.urls
