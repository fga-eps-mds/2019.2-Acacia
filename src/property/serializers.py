from rest_framework.serializers import ModelSerializer
from .models import Property

class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = (
            'type_of_address',
            'BRZipCode',
            'state',
            'city',
            'district',
            'address',
            'complement',
            'reference_point',
        )