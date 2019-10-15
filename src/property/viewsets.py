from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.models import User

from .models import Property
from .serializers import PropertySerializer
from .permissions import UserIsPropertyOwner

from localflavor.br.br_states import STATE_CHOICES

class PropertyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class =  PropertySerializer
    permission_classes = (IsAuthenticated, )

    # only this function is allowed without authentication
    def get(self, request, *args, **kwargs):
        """
        This endpoint returns an empty json with the 
        parameters needed to create a new user
        """

        required_fields = {'meta': 'the following fields are required'}
        required_fields.update(PropertySerializer().data)

        # this field only accepts values from this list
        options = [key for key, value in Property.TYPE_OF_ADDRESS]
        required_fields['type_of_address'] = {"options" : options}
        
        options = [key for key, value in STATE_CHOICES]
        required_fields['state'] = {"options" : options}

        return Response(required_fields)

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user.id)
    
    def perform_create(self, serializers):
        owner = User.objects.get(pk = self.request.user.id)
        serializers.save(owner = owner)
    
class PropertyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  PropertySerializer
    queryset = Property.objects.all()
    permission_classes = (IsAuthenticated, UserIsPropertyOwner)

    def get_queryset(self):
        return Property.objects.filter(owner=self.request.user.id)