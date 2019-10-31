from rest_framework.serializers import ModelSerializer

from django.utils.translation import ugettext as _
from .models import Property


class PropertySerializer(ModelSerializer):

    class Meta:
        model = Property
        fields = (
            'id',
            'type_of_address',
            'BRZipCode',
            'state',
            'city',
            'district',
            'address',
            'complement',
            'reference_point',
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
