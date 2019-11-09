from rest_framework.serializers import ModelSerializer, ValidationError
from tree.models import Tree, HarvestMonth
from django.utils.translation import ugettext as _


class HarvestMonthSerializer(ModelSerializer):
    class Meta:
        model = HarvestMonth
        fields = (
            'pk',
            'harvest_month',
        )

        extra_kwargs = {
            "harvest_month": {
                "error_messages": {
                    "required": _("Choose one of the "
                                  "following types: ") + str(
                                   HarvestMonth.valid_months()),

                    "invalid_choice":  _("Invalid type. "
                                         "Choose one of the following "
                                         "types: ") + str(
                                         HarvestMonth.valid_months()),
                }
            },
        }

    def validate_harvest_month(self, harvest_month):
        "Validates if this tree already has this month registered"

        pk_tree = self.context['view'].kwargs['tree_pk']

        month_queryset = HarvestMonth.objects.filter(
            tree=pk_tree,
            harvest_month=harvest_month
        )

        if month_queryset:
            raise ValidationError(
                'This tree already has this month registered'
            )

        return harvest_month


class TreeSerializer(ModelSerializer):

    harvest_months = HarvestMonthSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Tree
        fields = (
            'pk',
            'tree_type',
            'number_of_tree',
            'tree_height',
            'harvest_months',
        )

        extra_kwargs = {
            "tree_type": {
                "error_messages": {
                    "required": _("Choose one of the "
                                  "following types: ") + str(
                                   Tree.valid_tree_types()),

                    "invalid_choice":  _("Invalid type. "
                                         "Choose one of the following "
                                         "types: ") + str(
                                         Tree.valid_tree_types()),
                }
            },
        }

    def validate_tree_type(self, tree_type):
        "Validates if this property already has this tree type registered"
        pk_property = self.context['view'].kwargs['property_pk']
        tree_queryset = Tree.objects.filter(
            property=pk_property,
            tree_type=tree_type
        )

        if tree_queryset:
            raise ValidationError(
                'This property already has a tree of this type registered'
            )

        return tree_type
