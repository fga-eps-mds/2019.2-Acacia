from rest_framework.test import APITestCase
from django.urls import reverse
from datetime import datetime, timedelta

from property.models import Property
from users.models import User
from harvest.models import Harvest


class HarvestViewSetTestCase(APITestCase):

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

        self.property = Property.objects.get(pk=1)

    def setUp(self):
        self.create_user()
        self.create_property()

        self.harvest_data = {
            'date': '2019-11-18',
            'description': 'Apple Harvest',
            'status': 'Open',
            'max_volunteers': 10,
            'min_volunteers': 5,
        }

        self.url_list = reverse(
            'property:harvest:harvest-list',
            kwargs={'property_pk': self.property.pk}
        )

        self.url_detail = reverse(
            'property:harvest:harvest-detail',
            kwargs={
                'property_pk': self.property.pk,
                'pk': '1'
            }
        )

    def tearDown(self):
        Property.objects.all().delete()
        User.objects.all().delete()
        Harvest.objects.all().delete()

    def test_create_harvest(self):

        response = self.client.post(
            path=self.url_list,
            data=self.harvest_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Failed to create a harvest'
        )

        self.assertDictContainsSubset(
            self.harvest_data,
            response.data,
        )

        self.assertEqual(
            response.data['rules'],
            []
        )

        self.harvest = Harvest.objects.get(pk=1)

    def test_create_harvest_with_inconsistent_qnt_volunteers(self):

        self.harvest_data['min_volunteers'] = 10
        self.harvest_data['max_volunteers'] = 5

        response = self.client.post(
            path=self.url_list,
            data=self.harvest_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            400,
        )

    def test_create_harvest_rule(self):

        self.test_create_harvest()

        rule_url_list = reverse(
            'property:harvest:harvest_rules-list',
            kwargs={
                'property_pk': self.property.pk,
                'harvest_pk': self.harvest.pk
            }
        )

        response = self.client.post(
            path=rule_url_list,
            data={'description': 'To participate you need to like Vitas'},
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            201,
            msg='Failed to create a harvest rule'
        )

        self.assertEqual(
            'To participate you need to like Vitas',
            response.data['description'],
        )

    def test_create_two_identical_harvest_rule(self):

        self.test_create_harvest_rule()

        with self.assertRaises(AssertionError):
            self.test_create_harvest_rule()

    def test_get_harvests_of_the_week(self):

        today = datetime.date(datetime.now())

        # create harvests in the next 14 days
        for i in range(14):
            date = today + timedelta(days=i)

            self.harvest_data['date'] = date

            response = self.client.post(
                path=self.url_list,
                data=self.harvest_data,
                format='json',
                **self.credentials,
            )

            self.assertEqual(
                response.status_code,
                201,
                msg='Failed to create a harvest'
            )

        weekly_harvests_url = reverse(
            'weekly_harvests',
        )

        response = self.client.get(
            path=weekly_harvests_url,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            len(response.data),
            8,
            msg='Failed return only the next 7 days harvests'
        )

    def test_list_all_harvest(self):

        self.test_create_harvest()

        response = self.client.get(
            path=self.url_list,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            len(response.data),
            1,
            msg='More than one harvest was created'
        )

        response_data = dict(response.data[0])

        self.assertDictContainsSubset(
            self.harvest_data,
            response_data,
        )

    def test_patch_update_harvest(self):

        self.test_create_harvest()

        harvest_update = {
            'status': 'Done',
        }

        response = self.client.patch(
            path=self.url_detail,
            data=harvest_update,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update the harvest'
        )

        self.assertEqual(
            response.data['status'],
            harvest_update['status'],
        )

    def test_patch_update_harvest_with_inconsistent_qnt_volunteers(self):

        self.test_create_harvest()

        harvest_update = {
            'max_volunteers': 1,
        }

        response = self.client.patch(
            path=self.url_detail,
            data=harvest_update,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            400,
        )

    def test_patch_update_harvest_with_valid_qnt_volunteers(self):

        self.test_create_harvest()

        harvest_update = {
            'max_volunteers': 20,
            'min_volunteers': 10,
        }

        response = self.client.patch(
            path=self.url_detail,
            data=harvest_update,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update the harvest'
        )

    def test_put_update_harvest(self):

        self.test_create_harvest()

        self.harvest_data['status'] = 'Done'

        response = self.client.put(
            path=self.url_detail,
            data=self.harvest_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to update the harvest'
        )

        self.assertDictContainsSubset(
            self.harvest_data,
            response.data,
        )

    def test_get_harvest(self):

        self.test_create_harvest()

        response = self.client.get(
            path=self.url_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to get the harvest'
        )

        self.assertDictContainsSubset(
            self.harvest_data,
            response.data,
        )

    def test_delete_harvest(self):

        self.test_create_harvest()

        response = self.client.delete(
            path=self.url_detail,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            204,
            msg='Failed to delete the harvest'
        )

        harvests = Harvest.objects.all()
        qnt_harvest = len(harvests)

        self.assertEqual(
            qnt_harvest,
            0,
            msg='Failed to delete the harvest'
        )


class MonthlyHarvestsTestCase(APITestCase):

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

        self.property = Property.objects.get(pk=1)

    def setUp(self):
        self.create_user()
        self.create_property()

        self.harvest_data = {
            'date': '2019-11-21',
            'description': 'Apple Harvest',
            'status': 'Open',
            'max_volunteers': 10,
            'min_volunteers': 5,
        }

        self.url_list = reverse(
            'property:harvest:harvest-list',
            kwargs={'property_pk': self.property.pk}
        )

        self.url_detail = reverse(
            'property:harvest:harvest-detail',
            kwargs={
                'property_pk': self.property.pk,
                'pk': '1'
            }
        )

    def tearDown(self):
        Property.objects.all().delete()
        User.objects.all().delete()
        Harvest.objects.all().delete()

    def test_get_harvests_of_the_week(self):

        today = datetime.date(datetime(2020, 1, 1))

        for i in range(0, 12):
            date = today + timedelta(days=i*31)

            self.harvest_data['date'] = date

            response = self.client.post(
                path=self.url_list,
                data=self.harvest_data,
                format='json',
                **self.credentials,
            )

            self.assertEqual(
                response.status_code,
                201,
                msg='Failed to create a harvest'
            )

        for month in range(1, 13):
            weekly_harvests_url = reverse(
                'monthly_harvest',
                kwargs={
                    'year': date.year,
                    'month': month
                }
            )

            response = self.client.get(
                path=weekly_harvests_url,
            )

            self.assertEqual(
                len(response.data),
                1,
                msg='Failed return only 1 harvest'
            )
