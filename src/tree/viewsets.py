from rest_framework.viewsets import ModelViewSet
from tree.models import Tree
from tree.serializers import TreeSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

class TreeViewSet(ModelViewSet):
    
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    
    # permission_class = (IsAuthenticated,)
  