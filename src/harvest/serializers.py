
# Django
from django.conf import settings

# Models
from .models import Harvest

# Django Rest Framework
from rest_framework import serializers


class HarvestCreateSerializer(serializers.Serializer):

    date = serializers.DateField(
        required=True,
        label="Harvest Date",
    )

    rules = serializers.CharField(
        required=False,
        label="Harvest Rules",
    )

    description = serializers.CharField(
        required=True,
        label="Harvest Description",
    )

    max_volunteers = serializers.IntegerField(
        required=True,
        label="Harvest Max Volunteer Count",
    )

    equipment = serializers.CharField(
        required=False,
        label="Harvest Equipment", 
    )

    class Meta:
        model = Harvest
        fields = ['date', 'rules', 'description', 'max_volunteers', 'equipment']

    def create(self, validated_data):
        harvest = Harvest(**validated_data)
        harvest.save()
        return harvest

class HarverstModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = [
            'date', 
            'rules',
            'status',
            'neighbor_access', 
            'description', 
            'max_volunteers', 
            'equipment'
        ]