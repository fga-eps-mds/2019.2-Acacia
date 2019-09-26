from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer

class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        data = serializer.data

        # TODO: ADD TOKEN

        headers = self.get_success_headers(serializer.data)

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
