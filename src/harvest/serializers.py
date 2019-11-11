# Models
from .models import Harvest, RulesHarvest
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError
)


class RulesHarvestSerializer(ModelSerializer):
    class Meta:
        model = RulesHarvest
        fields = (
            'pk',
            'description',
        )


class HarvestSerializer(ModelSerializer):

    rules = RulesHarvestSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Harvest
        fields = (
            'pk',
            'date',
            'status',
            # 'equipment',
            'description',
            'max_volunteers',
            'min_volunteers',
            'rules',
        )

    def validate(self, data):

        min_volunteers = data['min_volunteers']
        max_volunteers = data['max_volunteers']

        if max_volunteers < min_volunteers:
            raise ValidationError(
                ("Minimum number of volunteers must be " +
                "less than maximum number of volunteers")
            )

        return data
