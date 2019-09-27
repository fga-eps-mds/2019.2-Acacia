import json

from rest_framework.test import APITestCase
from django.urls import reverse


class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse('users:signup')

    def test_different_password_on_password_confirmation(self):
        """
        Test to try to create a user with a wrong verification password
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
        Test to try to create a user with a password less than 8 characters
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

        user_data = {
            "username": "vitas",
            "email": "vitas@iAmGreat.com",
            "password": "VitasIsAwesome",
            "confirm_password": "VitasIsAwesome"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)

        user_data = {
            "username": "Reanu_Reves",
            "email": "vitas@iAmGreat.com",
            "password": "cyberpunk2077",
            "confirm_password": "cyberpunk2077"
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_unique_username_validation(self):
        """
        Test to try to create a user with a registered username
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