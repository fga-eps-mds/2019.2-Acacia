# Django
from django.conf import settings
from django.utils.translation import ugettext as _

# Models
from .models import Harvest

# Django Rest Framework=
from rest_framework.serializers import ModelSerializer, ReadOnlyField

class HarvestSerializer(ModelSerializer):

    class Meta:
        model = Harvest
        fields = (
            'date', 
            'status',
            'neighbor_access', 
            'description', 
            'max_volunteers', 
            'equipment'
        )

        # # Customizing error messages
        # extra_kwargs = {
        #     "type_of_address": {
        #         "error_messages": {
        #             "required": _("Choose one of the "
        #                 "following types: ") + str(
        #                     Property.valid_address()),

        #             "invalid_choice":  _("Invalid type. "
        #                 "Choose one of the following "
        #                     "types: ") + str(
        #                         Property.valid_address()),
        #         }
        #     },

        #     "state": {
        #         "error_messages": {
        #             "required": _("Choose one of the "
        #                 "following types: ") + str(
        #                     Property.valid_states()),
                    
        #             "invalid_choice":  _("Invalid type. "
        #                 "Choose one of the following "
        #                     "types: ") + str(
        #                         Property.valid_states()),
        #         }
        #     },
        # }


# class HarvestCreateSerializer(serializers.Serializer):

#     date = serializers.DateField(
#         required=True,
#         label="Harvest Date",
#     )

#     description = serializers.CharField(
#         required=True,
#         label="Harvest Description",
#     )

#     max_volunteers = serializers.IntegerField(
#         required=True,
#         label="Harvest Max Volunteer Count",
#     )

#     equipment = serializers.CharField(
#         required=False,
#         label="Harvest Equipment", 
#     )

#     class Meta:
#         model = Harvest
#         fields = ['date', 'description', 'max_volunteers', 'equipment']

#     def create(self, validated_data):
#         harvest = Harvest(**validated_data)
#         harvest.save()
#         return harvest

# class HarverstModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Harvest
#         fields = [

#         ]