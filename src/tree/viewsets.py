from rest_framework.viewsets import ModelViewSet
from tree.models import Tree
from tree.serializers import TreeSerializer

class TreeViewSet(ModelViewSet):
    
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
  
  
    # permission_classes = [IsAccountAdminOrReadOnly]