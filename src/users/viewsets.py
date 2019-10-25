from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import User

from .serializers import UserSignUpSerializer, UserPreferedLanguage


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ])
def test_access_token(request):
    return Response({'token_status': 'OK'})


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
