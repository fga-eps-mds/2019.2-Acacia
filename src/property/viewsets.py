from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import UserIsPropertyOwner
from .serializers import PropertySerializer
from users.models import User
from .models import Property


class PropertyViewSet(ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    pk_url_kwarg = 'property_pk'

    permission_classes = (
        IsAuthenticated,
        UserIsPropertyOwner
    )

    def get_queryset(self):
        return Property.objects.filter(
            owner=self.request.user.id
        )

    def perform_create(self, serializers):
        owner = User.objects.get(pk=self.request.user.id)
        serializers.save(owner=owner)
