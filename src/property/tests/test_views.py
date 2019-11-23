from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from django.urls import reverse

from property import viewsets
from property.models import Property
from property.permissions import UserIsPropertyOwner

from users.models import User


class PropertyListCreateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='vitas',
            email='vitas@vitas.com',
            password='vitasIsNice'
        )

        self.data = {
            'type_of_address': 'House',
            'BRZipCode': '73021498',
            'state': 'DF',
            'city': 'Gama',
            'district': 'Leste',
            'address': "Quadra 4",
        }

        self.view_detail = viewsets.PropertyViewSet.as_view({
            'delete': 'destroy',
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
        })

        self.view_list = viewsets.PropertyViewSet.as_view({
            'post': 'create',
            'get': 'list',
        })

        self.factory = APIRequestFactory()

        self.property = Property.objects.create(
            owner=self.user,
            **self.data,
        )

        self.url_detail = reverse(
            'property:property-detail',
            kwargs={'pk': self.property.pk}
        )

        self.url_list = reverse(
            'property:property-list',
        )

    def test_create_property(self):
        # changing zip code to create a unique property
        self.data['BRZipCode'] = '73021499'
        request = self.factory.post(self.url_list, self.data)
        force_authenticate(request, user=self.user)
        response = self.view_list(request)
        self.assertEqual(201, response.status_code)

    def test_create_property_with_same_unique_key(self):
        # changing zip code to create a unique property
        request = self.factory.post(self.url_list, self.data)
        force_authenticate(request, user=self.user)
        response = self.view_list(request)
        self.assertEqual(400, response.status_code)

    def test_list_property(self):
        request = self.factory.get(self.url_list)
        force_authenticate(request, user=self.user)
        response = self.view_list(request)
        data = {k: v for k, v in response.data[0].items()}
        self.assertDictContainsSubset(self.data, data)

    def test_delete_property(self):
        request = self.factory.delete(self.url_detail)
        force_authenticate(request, user=self.user)
        response = self.view_detail(
            request,
            pk=self.property.pk
        )
        self.assertEqual(204, response.status_code)

    def test_delete_property_without_authentication(self):
        request = self.factory.delete(self.url_detail)
        response = self.view_detail(
            request,
            pk=self.property.pk
        )
        self.assertEqual(401, response.status_code)

    def test_retrieve_property(self):
        request = self.factory.get(self.url_detail)
        force_authenticate(request, user=self.user)
        response = self.view_detail(
            request,
            pk=self.property.pk
        )
        self.assertEqual(200, response.status_code)
        self.assertDictContainsSubset(self.data, response.data)

    def test_patch_update_property(self):
        request = self.factory.patch(
            self.url_detail,
            {'state': 'GO'}
        )
        force_authenticate(request, user=self.user)
        response = self.view_detail(
            request,
            pk=self.property.pk
        )
        self.assertEqual(200, response.status_code)

        self.data['state'] = 'GO'

        self.assertEqual(
            response.data['state'],
            self.data['state']
        )

        self.assertDictContainsSubset(self.data, response.data)

    def test_put_update_property(self):
        self.data['state'] = 'GO'
        self.data['city'] = 'Damianópolis'
        request = self.factory.put(self.url_detail, self.data)
        force_authenticate(request, user=self.user)

        response = self.view_detail(
            request,
            pk=self.property.pk
        )

        self.assertEqual(200, response.status_code)

        self.assertEqual(
            response.data['state'],
            self.data['state']
        )

        self.assertDictContainsSubset(self.data, response.data)

    def test_read_only_permission(self):

        another_user = User.objects.create(
            username='MrRobot',
            email='robot@mr.com',
            password='hackerman'
        )

        request = self.factory.get(self.url_detail)
        force_authenticate(request, user=another_user)

        permission = UserIsPropertyOwner()
        ans = permission.has_object_permission(
            request,
            self.view_detail,
            self.property
        )

        self.assertTrue(
            ans
        )
