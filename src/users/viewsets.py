
# Django Rest Framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Models
from .models import User, Profile

# Serializers
from .serializers import UserSignUpSerializer, ProfileModelSerializer

#Permissions
from .permissions import IsOwner


class UserRegistrationAPIView(CreateAPIView):
    """
    Endpoint for user registration
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()

class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    """
    Endpoint for profile updated
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileModelSerializer

    def get_queryset(self):
        
        return Profile.objects.get(user=self.request.user.id)
    
    def get_object(self):
        queryset = self.get_queryset()

        return queryset

    def perform_update(self, serializers):
        user = User.objects.get(pk = self.request.user.id)
        serializers.save(user = user)