from rest_framework.serializers import ModelSerializer
from tree.models import Tree, HarvestMonth


class HarvestMonthSerializer(ModelSerializer):
    class Meta:
        model = HarvestMonth
        fields = (
            'harvest_month',
        )


class TreeSerializer(ModelSerializer):

    harvest_months = HarvestMonthSerializer(many=True)

    class Meta:
        model = Tree
        fields = (
            'id',
            'tree_type',
            'number_of_tree',
            'height_fruit',
            'harvest_months',
        )


    # def create(self, validated_data):
    #     harvest_months = validated_data.pop('harvest_months')
    #     tree = Tree.objects.create(**validated_data)

    #     for harvest_month in harvest_months:
    #         HarvestMonth.objects.create(
    #             property=tree,
    #             **harvest_month
    #         )

    #     return tree