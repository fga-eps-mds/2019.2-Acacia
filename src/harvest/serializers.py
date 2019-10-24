# Django
from django.conf import settings
from django.utils.translation import ugettext as _

# Models
from .models import Harvest, RulesHarvest

# Django Rest Framework
from rest_framework.serializers import ModelSerializer, ReadOnlyField

class RulesHarvestSerializer(ModelSerializer):
    class Meta:
        model = RulesHarvest
        fields = (
            'description',
        )

class HarvestSerializer(ModelSerializer):

    rules = RulesHarvestSerializer(
        many=True,
        write_only=True
    )

    class Meta:
        model = Harvest
        fields = (
            'date', 
            'status',
            'equipment',
            'description', 
            'max_volunteers', 
            'min_volunteers', 
            'rules',
        )

    def create(self, validated_data):
        rules = validated_data.pop('rules')
        harvest = Harvest.objects.create(**validated_data)

        for rule in rules:
            RulesHarvest.objects.create(
                harvest = harvest,
                **rule
            )
        
        return harvest