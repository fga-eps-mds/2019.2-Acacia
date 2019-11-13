
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Harvest, HarvestRules
from . import serializers
from property.models import Property


class HarvestViewSet(ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = serializers.HarvestSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    pk_url_kwarg = 'haverst_pk'

    def perform_create(self, serializer):

        property = Property.objects.get(
            id=self.kwargs['property_pk']
        )

        serializer.save(property=property)

    def get_queryset(self):
        return Harvest.objects.filter(
            property=self.kwargs['property_pk']
        )


class HarvestRulesViewSet(ModelViewSet):

    queryset = HarvestRules.objects.all()

    serializer_class = serializers.RulesHarvestSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):

        harvest = Harvest.objects.get(
            pk=self.kwargs['harvest_pk']
        )

        serializer.save(harvest=harvest)

    def get_queryset(self):
        return HarvestRules.objects.filter(
            harvest=self.kwargs['harvest_pk']
        )
