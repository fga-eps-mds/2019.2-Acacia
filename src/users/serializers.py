from .models import User
from rest_framework import serializers

class RegistrationUserSerializer(serializers.ModelSerializer):

    # password confirmation field
    password2 = serializers.CharField(
        style = { 'input_type': 'password' },
        write_only = True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
    
    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if len(password) < 8:
            raise serializers.ValidationError(
                { 'password': 'Password must be at least 8 characters.'}
            )
        
        if password != password2:
            raise serializers.ValidationError(
                { 'password': 'Passwords must match.'}
            )
        
        user.set_password(password)
        user.save()
        
        return user