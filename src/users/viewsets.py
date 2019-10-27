from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import User

from .serializers import UserSignUpSerializer, UserPreferedLanguage

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ])
def test_access_token(request):
    return Response({'token_status': 'OK'})


class CreateAccessToken(TokenObtainPairView):
    def get(self, request, *args, **kwargs):
        """
        This endpoint returns an empty json with the
        parameters needed to create a new user
        """

        required_fields = {
            'meta': 'The following fields are required in the request body',
            'email': '',
            'password': '',
        }

        return Response(required_fields)


class RefreshAccessToken(TokenRefreshView):
    def get(self, request, *args, **kwargs):
        """
        This endpoint returns an empty json with the
        parameters needed to create a new user
        """

        required_fields = {
            'meta': 'Refresh token sending`refresh token` in the request body',
            'refresh': '',
        }

        return Response(required_fields)


class UserRegistrationAPIView(CreateAPIView):
    """
    Endpoint for user registration
    """
    # by default all routes needs authentication
    permission_classes = (permissions.AllowAny, )

    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()


class RetrieveUpdatePreferedLanguageAPIView(RetrieveUpdateAPIView):
    """
    Returns a signed in users's prefered language
    """

    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserPreferedLanguage

    def update(self, request, *args, **kwargs):

        serializer = UserPreferedLanguage(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        user.chosen_language = serializer.data['chosen_language']
        user.save()

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
