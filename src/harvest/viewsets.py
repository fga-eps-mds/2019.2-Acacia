
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Harvest
from .serializers import HarvestSerializer
from property.models import Property


class HarvestViewSet(ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

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
