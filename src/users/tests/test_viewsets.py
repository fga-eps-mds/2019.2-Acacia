from rest_framework.test import APITestCase
from django.urls import reverse


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

        response = self.client.post(self.signup_url,user)

        self.assertEqual(
            response.status_code,
            201,
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


class ProfileUpdateAPIViewTestCase(APITestCase):

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

    def create_user(self, data=None):
        user_data = {
            'username': 'vitas',
            'email': 'vitas@vitas.com',
            'password': 'vitasIsNice',
            'confirm_password': 'vitasIsNice'
        }

        user_data = data if data else user_data

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

    def setUp(self):
        self.create_user()
        self.url_user_profile = reverse('users:profile_update')

    def test_get_user_profile(self):

        response = self.client.get(
            path=self.url_user_profile,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to get user profile data'
        )

        data = response.data

        self.assertEqual(
            data['bio'],
            '',
            msg='User profile bio isn\'t being set to empty by default'
        )

        self.assertEqual(
            data['username'],
            'vitas',
            msg='User username isn\'t being set correctly'
        )

        self.assertEqual(
            data['email'],
            'vitas@vitas.com',
            msg='User username isn\'t being set correctly'
        )

        self.assertIsNone(
            data['photo'],
            msg='Photo field not being set to None by default'
        )

        self.assertIsNone(
            data['birthdate'],
            msg='Birthdate field not being set to None by default'
        )

    def test_patch_update_user_profile(self):

        data = {
            'birthdate': '1990-01-01',
            'bio': ('Vitaliy Vladasovich Grachyov, better ' +
                     'known by his stage name Vitas, is a ' +
                     'Russian singer, author, composer and' +
                     ' actor.')
        }

        response = self.client.patch(
            path=self.url_user_profile,
            data=data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to patch update user profile'
        )

        self.assertEqual(
            response.data['birthdate'],
            data['birthdate'],
            msg='Failed set user birthdate'
        )

        self.assertEqual(
            response.data['bio'],
            data['bio'],
            msg='Failed set user bio'
        )

    def test_change_username_to_one_already_in_use(self):

        user_data = {
            'username': 'LeBron James',
            'email': 'lebron@james.com',
            'password': 'IamTheGoat',
            'confirm_password': 'IamTheGoat'
        }

        self.create_user(data=user_data)

        update_data = {
            'username': 'vitas' # that name is already in use
        }

        response = self.client.patch(
            path=self.url_user_profile,
            data=update_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            400,
        )

        self.assertEqual(
            str(response.data['username']),
            ("[ErrorDetail(string='This username is " +
             "already in use.', code='invalid')]"),
        )

    def test_get_prefered_language(self):

        url = reverse('users:set_prefered_language')

        response = self.client.get(
            path=url,
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertEqual(
            response.data['chosen_language'],
            'pt',
        )

    def test_update_prefered_language(self):

        url = reverse('users:set_prefered_language')

        data = {
            'chosen_language': 'en'
        }

        response = self.client.patch(
            path=url,
            data=data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertEqual(
            response.data['chosen_language'],
            'en',
        )

    def test_access_token(self):

        url = reverse('users:test_access_token')

        response = self.client.get(
            path=url,
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        response = self.client.get(
            path=url,
        )

        self.assertEqual(
            response.status_code,
            401,
        )

    def test_change_email_to_one_already_in_use(self):

        user_data = {
            'username': 'LeBron James',
            'email': 'lebron@james.com',
            'password': 'IamTheGoat',
            'confirm_password': 'IamTheGoat'
        }

        self.create_user(data=user_data)

        update_data = {
            'email': 'vitas@vitas.com', # that name is already in use
        }

        response = self.client.patch(
            path=self.url_user_profile,
            data=update_data,
            format='json',
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            400,
        )

        self.assertEqual(
            str(response.data['email']),
            ("[ErrorDetail(string='This email is " +
             "already in use.', code='invalid')]"),
        )

    def test_put_update_user_profile(self):

        data = {
            'username': 'LeBron James',
            'email': 'lebron@james.com',
            'birthdate': '1980-01-01',
            'bio': ('LeBron Raymone James Sr., is an ' +
                     'American professional basketball ' +
                     'player for the Los Angeles Lakers')
        }

        self.client.put(
            path=self.url_user_profile,
            data=data,
            format='json',
            **self.credentials,
        )

        response = self.client.get(
            path=self.url_user_profile,
            **self.credentials,
        )

        self.assertEqual(
            response.status_code,
            200,
            msg='Failed to put update user profile'
        )

        self.assertEqual(
            response.data['birthdate'],
            data['birthdate'],
            msg='Failed set user birthdate'
        )

        self.assertEqual(
            response.data['username'],
            data['username'],
            msg='Failed set user username'
        )

        self.assertEqual(
            response.data['email'],
            data['email'],
            msg='Failed set user email'
        )

        self.assertEqual(
            response.data['bio'],
            data['bio'],
            msg='Failed set user bio'
        )
