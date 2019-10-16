
# Django
from django.conf import settings

# Models
from .models import User, Profile

# Django Rest Framework
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
        #unique=True,
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

    #def validate_email(self, email):
    #    if User.objects.filter(email=email).exists():
    #        raise serializers.ValidationError('Email já cadastrado')
    #    return email


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
            raise serializers.ValidationError('Usuário com este nome já cadastrado')
        return username

    def create(self, validated_data):

        # this fields dont belongs to this class
        validated_data.pop('confirm_password')

        user = User.objects.create_user(**validated_data,
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
            'speaks_french',
            'speaks_english',
        ]


class ProfileModelSerializer(serializers.ModelSerializer):
    birthdate = serializers.DateField()
    phone_number = serializers.CharField()
    
    class Meta:
        model = Profile
        fields = [
            'photo',
            'birthdate',
            'bio',
            'phone_number',
            'is_owner',
            'is_volunteer',
            'is_leader',
        ]
    
    def validated_phone_number(self, phone_number):
        if phone_number.isdigit():
            return phone_number
        raise serializers.ValidationError('Número de telefone inválido')

    def validated_bio(self, bio):
        if len(bio) <= 140:
            return bio
        raise serializers.ValidationError('A Bio está com mais de 140 caracteres')

    def validated_birthdate(self, birthdate):
        if birthdate < date.today():
            return birthdate
        raise serializers.ValidationError('Data inválida')

    def update(self, instance, validated_data):
        
        
        if self.is_valid():
            instance.phone_number = self.validated_phone_number(validated_data['phone_number'])
            instance.photo = validated_data['photo']
            instance.is_leader = validated_data['is_leader']
            instance.is_owner = validated_data['is_owner']
            instance.is_volunteer = validated_data['is_volunteer']
            instance.bio = self.validated_bio(validated_data['bio'])
            instance.birthdate = self.validated_birthdate(validated_data['birthdate'])
            print(instance.phone_number)
            return instance