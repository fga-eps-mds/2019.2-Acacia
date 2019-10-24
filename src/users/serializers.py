from django.conf import settings
from django.utils.translation import ugettext as _

from .models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User

class UserSignUpSerializer(serializers.Serializer):

    username = serializers.CharField(
        required = True,
        label = _("Username"),

        validators = [
            UniqueValidator(
                queryset = User.objects.all(),
                message = _('This username is already registered')
            ),
        ],
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
        # unique=True,
        label="Email Address",
    )

    password = serializers.CharField(
        write_only = True,
        required = True,
        label = _("Password"),
        style = {'input_type': 'password'},
        min_length = 8,
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        label="Confirm Password",
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password', 
            'confirm_password'
        ]

    def validate_password(self, password):
        min_length = getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
        if len(password) < min_length:
            raise serializers.ValidationError(
                'Password must be at least %s characters' % (min_length)
            )
        return password

    def validate_confirm_password(self, password_confirmation):
        data = self.get_initial()
        password = data.get('password')
        if password != password_confirmation:
            raise serializers.ValidationError(_('Passwords must match'))
        return password_confirmation

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Usuário com este nome já cadastrado'
            )
        return username

    def create(self, validated_data):

        # this field should not be saved to database
        validated_data.pop('confirm_password')

        user = User.objects.create_user(
            **validated_data,
            is_verified=False
        )

        # TODO: SEND CONFIRMATION EMAIL

        return user


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'phone_number',
            'bio',
            'birth',
            'speaks_french',
            'speaks_english',
        ]


class UserPreferedLanguage(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['chosen_language']
