from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from django.urls import reverse

from tree import viewsets
from tree.models import Tree, HarvestMonth
from property.models import Property

from users.models import User


class PropertyListCreateAPIViewTestCase(APITestCase):

    def setUp(self):

        self.tree_view_detail = viewsets.TreeViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
        })

        self.tree_view_list = viewsets.TreeViewSet.as_view({
            'post': 'create',
            'get': 'list',
        })

        self.harvest_month_view_detail = viewsets.HarvestMonthViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
        })

        self.harvest_month_view_list = viewsets.HarvestMonthViewSet.as_view({
            'post': 'create',
            'get': 'list',
        })

        self.factory = APIRequestFactory()

        self.property_data = {
            'type_of_address': 'House',
            'BRZipCode': '73021498',
            'state': 'DF',
            'city': 'Gama',
            'district': 'Leste',
            'address': "Quadra 4",
        }

        self.tree_data = {
            'tree_type': 'Pequizeiro',
            'number_of_tree': 3,
            'tree_height': 20.5,
        }

        self.harvest_month_data = {
            'harvest_month': 'September'
        }

        self.user = User.objects.create(
            username='vitas',
            email='vitas@vitas.com',
            password='vitasIsNice'
        )

        self.property = Property.objects.create(
            owner=self.user,
            **self.property_data,
        )

        self.tree = Tree.objects.create(
            pk_property=self.property,
            **self.tree_data
        )

        self.harvest_month = HarvestMonth.objects.create(
            pk_tree=self.tree,
            **self.harvest_month_data,
        )

        self.url_detail = reverse(
            'property:tree:tree-detail',
            kwargs={
                'pk_property': 1,
                'pk_tree': self.tree.pk_tree
            }
        )

        self.url_list = reverse(
            'property:tree:tree-list',
            kwargs={'pk_property': 1}
        )

    # BUG -> Da maneira que o validação do serializer da
    # árvore foi feita não é testável pela request que o
    # APIRequestFactory gera.

    # Esse request não está "levando" o pk_property dentro do
    # kargs, e lá no serializer precisamos dele.

    # Já quando a requisição é feita pelo navegador, esse
    # parâmetro aparece no kwargs.

    # Eu desconfio que exista uma maneira melhor de validar
    # esse serializer

    def test_create_property(self):
        # changing zip code to create a unique property
        self.tree_data['tree_type'] = 'Papaya'
        request = self.factory.post(self.url_list, self.tree_data)
        force_authenticate(request, user=self.user)
        response = self.tree_view_list(request)
        self.assertEqual(201, response.status_code)