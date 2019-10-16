
# Django Rest Framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer

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

class GetUserPreferedLanguage(CreateAPIView):
    """
    Returns a signed in users's prefered language
    """
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        return Response({
            'chosen_language': request.user.chosen_language
        })

class SetUserPreferedLanguage(CreateAPIView):
    """
    Sets a signed in users's prefered language
    """
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        if not 'chosen_language' in request.data:
          return Response({
            'message': "No 'chosen_language' attribute found in request"
          })
        request.user.chosen_language = request.data['chosen_language']
        request.user.save()
        return Response({
          'message': 'Language updated to ' + request.user.chosen_language
        })

class TestAccessToken(CreateAPIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        return Response({
            'message': 'valid'
        })