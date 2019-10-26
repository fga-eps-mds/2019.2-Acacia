from django.conf import settings

# Models
from .models import User, Profile

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from datetime import date


class UserSignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        label="Username",
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
        # unique=True,
        label="Email Address",
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        label="Password",
        style={'input_type': 'password'},
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        label="Confirm Password",
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate_password(self, password):
        min_length = getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
        if len(password) < min_length:
            raise serializers.ValidationError(
                'A senha deve ter no mínimo %s caracteres' % (min_length)
            )
        return password

    def validate_confirm_password(self, password_confirmation):
        data = self.get_initial()
        password = data.get('password')
        if password != password_confirmation:
            raise serializers.ValidationError('As senhas devem corresponder')
        return password_confirmation

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Usuário com este nome já cadastrado'
            )
        return username

    def create(self, validated_data):

        # this fields dont belongs to this class
        validated_data.pop('confirm_password')

        user = User.objects.create_user(
            **validated_data,
            is_verified=False
        )

        Profile.objects.create(user=user)

        # TODO: SEND CONFIRMATION EMAIL

        return user


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'speaks_french',
            'speaks_english',
        ]


class ProfileModelSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = [
            'photo',
            'birthdate',
            'bio',
            'phone_number',
            'email',
            'username',
        ]

    def check_if_is_unique(self, field, field_name):
        """
        This method uses class meta data to
        checks if the field is unique on database

        Args:
            field (string): field value from Profile Serializer
            field_name (string): field name from Profile model

        Raises:
            ValidationError: this field is already in use

        Returns:
            string: same field passed as argument
        """

        current_field = self.instance.user.__dict__.get(field_name)

        filter_params = {
            (field_name + '__iexact'): field
        }

        exclude_params = {
            (field_name + '__iexact'): current_field
        }

        # lookin if there is any user registered
        # with the new field
        user = User.objects.filter(
            **filter_params
        ).exclude(**exclude_params)

        if user:
            raise serializers.ValidationError(
                f'This {field_name} is already in use.'
            )

        return field

    def validate_email(self, email):
        return self.check_if_is_unique(email, 'email')

    def validate_username(self, username):
        return self.check_if_is_unique(username, 'username')

    def validate_phone_number(self, phone_number):
        if phone_number.isdigit():
            return phone_number
        raise serializers.ValidationError('Invalid phone number')

    def validate_bio(self, bio):
        if len(bio) <= 140:
            return bio
        raise serializers.ValidationError(
            'Bio field is longer than 140 characters'
        )

    def validate_birthdate(self, birthdate):
        if birthdate < date.today():
            return birthdate
        raise serializers.ValidationError('Invalid Date')

class UserPreferedLanguage(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['chosen_language']
