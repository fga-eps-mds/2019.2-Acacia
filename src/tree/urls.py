from . import viewsets
from django.urls import path, include
from rest_framework import routers


app_name = 'tree'

tree_router = routers.SimpleRouter()
tree_router.register(r'', viewsets.TreeViewSet, basename='tree')

tree_slashless_router = routers.DefaultRouter(trailing_slash=False)
tree_slashless_router.registry = tree_router.registry[:]


harvest_month_router = routers.SimpleRouter()
harvest_month_router.register(
    r'',
    viewsets.HarvestMonthViewSet,
    basename='harvest_months'
)

harvest_month_slashless_router = routers.DefaultRouter(trailing_slash=False)
harvest_month_slashless_router.registry = harvest_month_router.registry[:]

urlpatterns = [
    path(
        '<int:tree_pk>/harvest_months/',
        include(harvest_month_router.urls),
    ),

    path(
        '<int:tree_pk>/harvest_months',
        include(harvest_month_router.urls),
    ),
]

urlpatterns += tree_router.urls
urlpatterns += tree_slashless_router.urls
urlpatterns += harvest_month_slashless_router.urls
