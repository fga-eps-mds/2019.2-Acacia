from .models import User

from .serializers import RegistrationUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationUserSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'Sucessfully registered a new user.'
        data['email'] = user.email
        data['username'] = user.username
    
    else:
        data = serializer.errors
    
    return Response(data)