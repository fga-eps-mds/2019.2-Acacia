from rest_framework.viewsets import ModelViewSet

from .serializers import PictureSerializer
from .models import Picture

class PictureViewSet(ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()
    