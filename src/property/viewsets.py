from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.models import User

from .models import Property
from .serializers import PropertySerializer
from .permissions import UserIsOwnerProperty

class PropertyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class =  PropertySerializer

    def get(self, request, *args, **kwargs):
        return Response({'test':'test'})

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user.id)
    
    def perform_create(self, serializers):
        owner = User.objects.get(pk = self.request.user.id)
        serializers.save(owner = owner)
    
class PropertyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  PropertySerializer
    queryset = Property.objects.all()
    permission_classes = (UserIsOwnerProperty, )

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user.id)

