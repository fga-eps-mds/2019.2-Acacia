from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from tree.models import Tree, HarvestMonth
from property.models import Property
from tree import serializers


class TreeViewSet(ModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = serializers.TreeSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    # TODO: if not authenticate, readonly
    permission_class = (IsAuthenticated,)

    # override default pk model attribute
    pk_url_kwarg = 'tree_pk'

    def perform_create(self, serializer):
        property = Property.objects.get(
            id=self.kwargs['property_pk']
        )

        serializer.save(property=property)

    def get_queryset(self):
        return Tree.objects.filter(
            property=self.kwargs['property_pk']
        )


class HarvestMonthViewSet(ModelViewSet):
    queryset = HarvestMonth.objects.all()
    serializer_class = serializers.HarvestMonthSerializer

    # TODO: if not authenticate, readonly
    permission_class = (IsAuthenticated,)

    # override default pk model attribute
    lookup_field = 'pk'

    def perform_create(self, serializer):

        tree = Tree.objects.get(
            pk=self.kwargs['tree_pk']
        )

        serializer.save(tree=tree)

    def get_queryset(self):
        return HarvestMonth.objects.filter(
            tree=self.kwargs['tree_pk']
        )
