from rest_framework.test import APITestCase
from django.urls import reverse
from tree.models import Tree
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

    def setUp(self):

        self.create_user()
        self.create_property()

        self.tree_data = {
            'tree_type': 'Pequizeiro',
            'number_of_tree': 3,
            'tree_height': 20.5,
        }

        self.url_list = reverse(
            'property:tree:tree-list',
            kwargs={'pk_property': 1}
        )

        self.url_detail = reverse(
            'property:tree:tree-detail',
            kwargs={'pk_property': 1, 'pk_tree': 1}
        )

    def test_create_tree(self):
        response = self.client.post(
            path=self.url_list,
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

    def test_list_all_trees(self):

        self.test_create_tree()

        response = self.client.get(
            path=self.url_list,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            len(response.data),
            1,
            msg='More than one tree was created'
        )

        response_data = dict(response.data[0])
        tree_data = self.tree.__dict__

        self.assertEqual(
            str(tree_data['tree_height']),
            str(response_data['tree_height']),
        )

        self.assertEqual(
            tree_data['pk_tree'],
            response_data['pk_tree'],
        )

        self.assertEqual(
            tree_data['tree_type'],
            response_data['tree_type'],
        )

        self.assertEqual(
            tree_data['number_of_tree'],
            response_data['number_of_tree'],
        )

    def test_patch_update_tree(self):
        self.test_create_tree()

        # partial update
        tree_update = {
            'tree_type': 'Banana'
        }

        response = self.client.patch(
            path=self.url_detail,
            data=tree_update,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch updade the tree'
        )

        self.tree = Tree.objects.last()

    def test_put_update_tree(self):
        self.test_create_tree()

        # complete update (all fields)
        self.tree_data['tree_type'] = 'Banana'

        response = self.client.put(
            path=self.url_detail,
            data=self.tree_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to update the tree'
        )

        self.tree = Tree.objects.last()

    def test_get_tree(self):
        self.test_create_tree()

        response = self.client.get(
            path=self.url_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to get the tree'
        )

        self.assertEqual(
            str(self.tree_data['tree_height']),
            response.data['tree_height'],
        )

        self.assertEqual(
            str(self.tree_data['tree_type']),
            response.data['tree_type'],
        )

        self.assertEqual(
            response.data['pk_tree'],
            1,
        )

        self.assertEqual(
            self.tree_data['number_of_tree'],
            response.data['number_of_tree'],
        )

    def test_delete_tree(self):
        self.test_create_tree()

        response = self.client.delete(
            path=self.url_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            204,
            msg='Failed to delete the tree'
        )

        trees = Tree.objects.all()
        qnt_trees = len(trees)

        self.assertEqual(
            qnt_trees,
            0,
            msg='Failed to delete the tree'
        )
