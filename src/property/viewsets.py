from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from users.models import User

from .serializers import PropertySerializer
from .permissions import UserIsPropertyOwner
from .models import Property


class PropertyViewSet(ModelViewSet):
    serializer_class =  PropertySerializer
    queryset = Property.objects.all()
    
    permission_classes = (
        IsAuthenticated, 
        UserIsPropertyOwner
    )

    def get_queryset(self):
        return Property.objects.filter(
            owner=self.request.user.id
        )
    
    def perform_create(self, serializers):
        owner = User.objects.get(pk = self.request.user.id)
        serializers.save(owner = owner)
