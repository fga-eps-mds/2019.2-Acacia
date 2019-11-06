from rest_framework.serializers import ModelSerializer

from django.utils.translation import ugettext as _
from .models import Property

from tree.serializers import TreeSerializer


class PropertySerializer(ModelSerializer):

    trees = TreeSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Property
        fields = (
            'pk_property',
            'type_of_address',
            'BRZipCode',
            'state',
            'city',
            'district',
            'address',
            'complement',
            'reference_point',
            'trees',
        )

        # Customizing error messages
        extra_kwargs = {
            "type_of_address": {
                "error_messages": {
                    "required": _("Choose one of the "
                                  "following types: ") + str(
                                   Property.valid_address()),

                    "invalid_choice":  _("Invalid type. "
                                         "Choose one of the following "
                                         "types: ") + str(
                                         Property.valid_address()),
                }
            },

            "state": {
                "error_messages": {
                    "required": _("Choose one of the "
                                  "following types: ") + str(
                                  Property.valid_states()),

                    "invalid_choice":  _("Invalid type. "
                                         "Choose one of the following "
                                         "types: ") + str(
                                         Property.valid_states()),
                }
            },
        }
