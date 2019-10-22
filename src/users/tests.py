from rest_framework.test import APITestCase
from django.urls import reverse
from django.db import IntegrityError


class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse('users:register')

    def test_different_password_on_password_confirmation(self):
        """
        Test to try to create a user with a
        wrong verification password
        """

        user_data = {
            "username": "vitas",
            "email": "vitas@iAmGreat.com",
            "password": "VitasIsNice",
            "confirm_password": "VitasIsAwesome"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_password_less_than_8_characters(self):
        """
        Test to try to create a user with a
        password less than 8 characters
        """

        user_data = {
            "username": "vitas",
            "email": "vitas@iAmGreat.com",
            "password": "HiVitas",
            "confirm_password": "HiVitas"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_unique_email_validation(self):
        """
        Test to try to create a user with a registered email
        """

        user1_data = {
            "username": "vitas",
            "email": "vitas@iAmGreat.com",
            "password": "VitasIsAwesome",
            "confirm_password": "VitasIsAwesome"
        }
        user2_data = {
            "username": "Reanu_Reves",
            "email": "vitas@iAmGreat.com",
            "password": "cyberpunk2077",
            "confirm_password": "cyberpunk2077"
        }
        response = self.client.post(self.url, user1_data)

        self.assertEqual(201, response.status_code)

        with self.assertRaises(IntegrityError):
            response = self.client.post(self.url, user2_data)

    def test_unique_username_validation(self):
        """
        Test to try to create a user with
        a registered username
        """

        user_data = {
            "username": "vitas",
            "email": "vitas@iAmGreat.com",
            "password": "VitasIsAwesome",
            "confirm_password": "VitasIsAwesome"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)

        user_data = {
            "username": "vitas",
            "email": "keanu@reeves.com",
            "password": "cyberpunk2077",
            "confirm_password": "cyberpunk2077"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):
        """
        Test to create a user with valid data
        """

        user_data = {
            "username": "keanu_reeves",
            "email": "keanu@reeves.com",
            "password": "cyberpunk2077",
            "confirm_password": "cyberpunk2077"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)


class UserAuthenticationAPIViewTestCase(APITestCase):
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

        self.assertEqual(
            201,
            self.client.post(
                self.signup_url,
                user
            ).status_code,
            msg='User setup failed'
        )

    def authenticate_user(self, user=user_cleber):
        """
        Authenticates a set up user and returns it's tokens
        """

        response = self.client.post(
            self.token_url,
            {
                "email": user['email'],
                "password": user['password']
            }
        )

        self.assertEqual(
            200,
            response.status_code,
            msg='User authentication failed'
        )

        return response.data

    def test_authenticate_valid_user(self):
        """
        Test authentication of valid user
        """

        self.create_user(self.user_cleber)

        authentication_data = {
            "email": self.user_cleber['email'],
            "password": self.user_cleber['password'],
        }

        response = self.client.post(
            self.token_url,
            authentication_data
        )

        self.assertEqual(200, response.status_code)

        self.assertIsNotNone(
            response.data['access'],
            msg='No access token found'
        )

        self.assertIsNotNone(
            response.data['refresh'],
            msg='No refresh token found'
        )

    def test_failed_password_authentication(self):
        """
        Tests if wrong password does now allow access to user
        """

        self.create_user(self.user_cleber)

        authentication_data = {
            "email": self.user_cleber['email'],
            "password": "asdfghjkl",  # Wrong password
        }

        response = self.client.post(
            self.token_url,
            authentication_data
        )

        self.assertEqual(
            401,
            response.status_code,
        )

    def test_failed_email_authentication(self):
        """
        Tests if wrong password does now allow access to user
        """

        self.create_user(self.user_cleber)

        authentication_data = {
            "email": 'batata@gmail.com',  # Wrong email
            "password": self.user_cleber['password'],
        }

        response = self.client.post(
            self.token_url,
            authentication_data
        )

        self.assertEqual(401, response.status_code)

    def test_get_access_token_from_valid_refresh_token(self):
        """
        Tests if a valid refresh token can get
        a new instance of a access token
        """

        self.create_user(self.user_cleber)
        tokens = self.authenticate_user(self.user_cleber)

        response = self.client.post(
            self.refresh_url,
            {"refresh": tokens['refresh']}
        )

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(
            response.data['access'],
            msg='No access token found'
        )
