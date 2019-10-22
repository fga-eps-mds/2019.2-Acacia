# Django
from django.conf import settings
from django.utils.translation import ugettext as _

# Models
from .models import Harvest

# Django Rest Framework
from rest_framework.serializers import ModelSerializer, ReadOnlyField

class HarvestSerializer(ModelSerializer):

    class Meta:
        model = Harvest
        fields = (
            'date', 
            'status',
            'neighbor_access', 
            'equipment',
            'description', 
            'max_volunteers', 
        )