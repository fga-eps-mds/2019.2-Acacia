
# Django Rest Framework
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Models
from .models import Harvest

# Serializers
from .serializers import HarvestSerializer


class HarvestViewSet(ModelViewSet):

    # TODO A Harvest belongs to a property

    serializer_class = HarvestSerializer
    queryset = Harvest.objects.all()
   
    permission_classes = (
        permissions.AllowAny,
    )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
