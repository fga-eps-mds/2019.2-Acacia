from django.urls import path, include
from rest_framework import routers
from . import viewsets


app_name = 'tree'

tree_router = routers.SimpleRouter()
tree_router.register(
	r'',
	viewsets.TreeViewSet,
	basename='tree'
)

harvest_month_router = routers.SimpleRouter()
harvest_month_router.register(
    r'',
    viewsets.HarvestMonthViewSet,
    basename='months'
)

urlpatterns = [
    path(
        '<int:tree_pk>/months/',
        include(harvest_month_router.urls),
    ),

] + tree_router.urls
