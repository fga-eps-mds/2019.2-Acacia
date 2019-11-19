# Models
from django.utils.translation import ugettext as _
from . import models
from rest_framework import serializers


class RulesHarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HarvestRules
        fields = (
            'pk',
            'description',
        )

    def validate_description(self, description):
        """
        Validates if this harvest already has
        this rule description
        """

        pk_harvest = self.context['view'].kwargs['harvest_pk']

        rule_queryset = models.HarvestRules.objects.filter(
            harvest=pk_harvest,
            description=description
        )

        if rule_queryset:
            raise serializers.ValidationError(
                'This harvest already has this rule description registered'
            )

        return description


class HarvestSerializer(serializers.ModelSerializer):

    rules = RulesHarvestSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Harvest
        fields = (
            'pk',
            'date',
            'status',
            'description',
            'max_volunteers',
            'min_volunteers',
            'rules',
            'property_id'
        )

        extra_kwargs = {
            "status": {
                "error_messages": {
                    "required": _("Choose one of the "
                                  "following status: ") + str(
                                   models.Harvest.valid_status()),

                    "invalid_choice":  _("Invalid status. "
                                         "Choose one of the following "
                                         "types: ") + str(
                                         models.Harvest.valid_status()),
                }
            },
        }

    def validate(self, data):
        """
        This validation occurs on both update and create
        requests, so you need to verify that the crop in
        question already exists before purchasing the number
        of volunteers.
        """

        min_volunteers = data.get('min_volunteers', None)
        max_volunteers = data.get('max_volunteers', None)

        # patch request that doesn't update this field
        if min_volunteers is None and max_volunteers is None:
            return data

        harvest_pk = self.context['view'].kwargs.get('pk', None)

        # patch or put request
        if harvest_pk:
            harvest = models.Harvest.objects.get(pk=harvest_pk)

            if not min_volunteers:
                min_volunteers = harvest.min_volunteers

            if not max_volunteers:
                max_volunteers = harvest.max_volunteers

        if max_volunteers < min_volunteers:
            raise serializers.ValidationError(
                ("Minimum number of volunteers must be " +
                 "less than maximum number of volunteers")
            )

        return data
