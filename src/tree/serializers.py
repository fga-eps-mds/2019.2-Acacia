from rest_framework.serializers import ModelSerializer
from tree.models import Tree
# from users.serializers import UserSignUpSerializer

# from property.model import Property

class TreeSerializer(ModelSerializer):
    
    # owner = UserSignUpSerializer()
    
    class Meta:
        model = Tree
        fields = ( 
            'id',
            'tree_type',
            'number_of_tree',
            'height_fruit',
            'matury_date',
            'haverst_for_year',
            # 'owner',
            'tree_picture',
        )