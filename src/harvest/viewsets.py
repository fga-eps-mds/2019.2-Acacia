
# Django Rest Framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

# Models
from .models import Harvest

# Serializers
from .serializers import HarvestCreateSerializer

from rest_framework.decorators import api_view

class HarvestCreateAPIView(CreateAPIView):
    """
    Endpoint for user registration
    """

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = HarvestCreateSerializer
    queryset = Harvest.objects.all()
