from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from tree.models import Tree, HarvestMonth
from property.models import Property
from tree import serializers


class TreeViewSet(ModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = serializers.TreeSerializer
    permission_class = (IsAuthenticated,)
    lookup_field = 'pk_tree'

    def perform_create(self, serializer):

        property = Property.objects.get(
            pk_property=self.kwargs['pk_property']
        )

        serializer.save(pk_property=property)

    def get_queryset(self):
        return Tree.objects.filter(
            pk_property=self.kwargs['pk_property']
        )


class HarvestMonthViewSet(ModelViewSet):
    queryset = HarvestMonth.objects.all()
    serializer_class = serializers.HarvestMonthSerializer
    permission_class = (IsAuthenticated,)
    lookup_field = 'pk_harvest_month'

    def perform_create(self, serializer):

        tree = Tree.objects.get(
            pk_tree=self.kwargs['pk_tree']
        )

        serializer.save(pk_tree=tree)

    def get_queryset(self):
        return HarvestMonth.objects.filter(
            pk_tree=self.kwargs['pk_tree']
        )
