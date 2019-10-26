from rest_framework.serializers import ModelSerializer
from tree.models import Tree

class TreeSerializer(ModelSerializer):
    class Meta:
        model = Tree
        fields = ['id', 'tree_type', 'number_of_tree', 'matury_date']