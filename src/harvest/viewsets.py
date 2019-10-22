
# Django Rest Framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

# Models
from .models import Harvest

# Serializers
from .serializers import HarvestSerializer

from rest_framework.decorators import api_view

class HarvestViewSet(ModelViewSet):

    # TODO A Harvest belongs to a property

    serializer_class = HarvestSerializer
    queryset = Harvest.objects.all()
    
    permission_classes = (
        permissions.AllowAny, 
    )
    
    def perform_create(self, serializers):
        serializers.save()

# class HarvestViewSet(CreateAPIView):
#     """
#     Endpoint for harvest creation
#     """

#     permission_classes = (permissions.IsAuthenticated, )
#     serializer_class = HarvestCreateSerializer
#     queryset = Harvest.objects.all()

# class HarvertInteract(RetrieveUpdateDestroyAPIView):
#     """
#     Endpoint for harvest update, delete or get
#     """

#     permission_classes = (permissions.IsAuthenticated, )
#     serializer_class = HarvestCreateSerializer
#     queryset = Harvest.objects.all()
