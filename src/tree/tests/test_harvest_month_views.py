from rest_framework.test import APITestCase
from django.urls import reverse
from tree.models import Tree, HarvestMonth
from property.models import Property


class TreeAPIViewTestCase(APITestCase):

    def create_authentication_tokens(self, user_credentials):
        url_token = reverse('users:token_obtain_pair')

        response = self.client.post(
            url_token,
            user_credentials,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to create user tokens credentials'
        )

        self.credentials = {
            'HTTP_AUTHORIZATION': 'Bearer ' + response.data['access']
        }

    def create_user(self):
        user_data = {
            "username": 'vitas',
            'email': 'vitas@vitas.com',
            'password': 'vitasIsNice',
            'confirm_password': 'vitasIsNice'
        }

        url_user_signup = reverse('users:register')

        response = self.client.post(
            url_user_signup,
            user_data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Failed during user creation'
        )

        user_data.pop('username')
        user_data.pop('confirm_password')

        self.create_authentication_tokens(user_data)

    def create_property(self):
        property_data = {
            'type_of_address': 'House',
            'BRZipCode': '73021498',
            'state': 'DF',
            'city': 'Gama',
            'district': 'Leste',
            'address': "Quadra 4",
        }

        url_property_creation = reverse(
            'property:property-list',
        )

        response = self.client.post(
            path=url_property_creation,
            data=property_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Failed to create property'
        )

        self.property = Property.objects.last()

    def create_tree(self):
        self.tree_data = {
            'tree_type': 'Pequizeiro',
            'number_of_tree': 3,
            'tree_height': 20.5,
        }

        self.url_tree_list = reverse(
            'property:tree:tree-list',
            kwargs={'pk_property': 1}
        )

        response = self.client.post(
            path=self.url_tree_list,
            data=self.tree_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Failed to create a tree'
        )

        self.tree = Tree.objects.last()

    def setUp(self):
        self.create_user()
        self.create_property()
        self.create_tree()

        self.url_month_list = reverse(
            'property:tree:harvest_months-list',
            kwargs={'pk_property': 1, 'pk_tree': 1}
        )

        self.url_month_detail = reverse(
            'property:tree:harvest_months-detail',
            kwargs={
                'pk_property': 1,
                'pk_tree': 1,
                'pk_harvest_month': 1,
            }
        )

    def test_create_harvest_month(self):

        response = self.client.post(
            path=self.url_month_list,
            data={'harvest_month': 'May'},
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Failed to create a haverst month'
        )

        self.harvest_month = HarvestMonth.objects.last()

    def test_create_harvest_months_of_the_same(self):
        self.test_create_harvest_month()
        with self.assertRaises(AssertionError):
            self.test_create_harvest_month()

    def test_list_all_harvest_months(self):
        self.test_create_harvest_month()

        response = self.client.get(
            path=self.url_month_list,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            len(response.data),
            1,
            msg='More than one haverst month was created'
        )

        response_data = dict(response.data[0])
        harvest_month_data = { 'harvest_month': 'May' }

        self.assertEqual(
            harvest_month_data['harvest_month'],
            response_data['harvest_month'],
            msg=('The month registered is different from ' +
                'the month of the request')
        )

    def test_patch_update_harvest_months(self):
        self.test_create_harvest_month()

        response = self.client.patch(
            path=self.url_month_detail,
            data={'harvest_month': 'April'},
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update the haverst month'
        )

        self.harvest_month = Tree.objects.last()

    def test_put_update_harvest_months(self):
        self.test_create_harvest_month()

        response = self.client.put(
            path=self.url_month_detail,
            data={'harvest_month': 'April'},
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to put update the haverst month'
        )

        self.harvest_month = Tree.objects.last()


    def test_get_harvest_months(self):
        self.test_create_harvest_month()

        response = self.client.get(
            path=self.url_month_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to get the harvest months'
        )

        self.assertEqual(
            response.data['harvest_month'],
            'May'
        )

    def test_delete_harvest_months(self):
        self.test_create_harvest_month()

        response = self.client.delete(
            path=self.url_month_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            204,
            msg='Failed to delete the harvest months'
        )

        trees = HarvestMonth.objects.all()
        qnt_trees = len(trees)

        self.assertEqual(
            qnt_trees,
            0,
            msg='Failed to delete the harvest months'
        )
