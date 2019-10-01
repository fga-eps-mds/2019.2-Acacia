
# Django Rest Framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

# Models
from .models import User

# Serializers
from .serializers import UserSignUpSerializer


class UserRegistrationAPIView(CreateAPIView):
    """
    Endpoint for user registration
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()