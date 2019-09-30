import json

from rest_framework.test import APITestCase
from django.urls import reverse


class UserAuthenticationAPIViewTestCase(APITestCase):

    # SETUP


    signup_url = reverse('users:register')
    token_url = reverse('users:token_obtain_pair')
    refresh_url = reverse('users:token_refresh')

    user_cleber = {
        "username": "cleber",
        "email": "cleber@gmail.com",
        "password": "cleber123",
        "confirm_password": "cleber123"
    }


    def create_user(self, user=user_cleber):
        """
        Set's up user in database.
        """

        self.assertEqual(201, self.client.post(
            self.signup_url, user).status_code, msg='User setup failed')


    def authenticate_user(self, user=user_cleber):
        """
        Authenticates a set up user and returns it's tokens
        """

        response = self.client.post(
            self.token_url, {"email": user['email'], "password": user['password']})
        self.assertEqual(200, response.status_code, msg='User authentication failed')
        return response.data

    # TESTS


    def test_authenticate_valid_user(self):
        """
        Test authentication of valid user
        """

        self.create_user(self.user_cleber)

        authentication_data = {
            "email": self.user_cleber['email'],
            "password": self.user_cleber['password'],
        }

        response = self.client.post(self.token_url, authentication_data)
        self.assertEqual(200, response.status_code,
                        msg='Response not 200 (' + str(response.status_code) + ')')
        self.assertIsNotNone(response.data['access'], msg='No access token found')
        self.assertIsNotNone(response.data['refresh'], msg='No refresh token found')


    def test_failed_password_authentication(self):
        """
        Tests if wrong password does now allow access to user
        """

        self.create_user(self.user_cleber)

        authentication_data = {
            "email": self.user_cleber['email'],
            "password": "asdfghjkl",  # Wrong password
        }

        response = self.client.post(self.token_url, authentication_data)
        self.assertEqual(401, response.status_code, msg='Unexpected response code (' +
                        str(response.status_code) + '), expecting 401')


    def test_failed_email_authentication(self):
        """
        Tests if wrong password does now allow access to user
        """

        self.create_user(self.user_cleber)

        authentication_data = {
            "email": 'batata@gmail.com',  # Wrong email
            "password": self.user_cleber['password'],
        }

        response = self.client.post(self.token_url, authentication_data)
        self.assertEqual(401, response.status_code, msg='Unexpected response code (' +
                        str(response.status_code) + '), expecting 401')


    def test_get_access_token_from_valid_refresh_token(self):
        """
        Tests if a valid refresh token can get a new instance of a access token
        """

        self.create_user(self.user_cleber)
        tokens = self.authenticate_user(self.user_cleber)

        response = self.client.post(self.refresh_url, {"refresh": tokens['refresh']})
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.data['access'], msg='No access token found')
