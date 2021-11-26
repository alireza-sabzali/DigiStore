from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'access_token', 'refresh_token')
        read_only_fields = ('access_token', 'refresh_token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username        = serializers.CharField(max_length=255, read_only=True)
    password        = serializers.CharField(max_length=128, write_only=True)
    access_token    = serializers.CharField(max_length=255, read_only=True)
    refresh_token   = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        if data['password'] is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'username': user.username,
            'access_token': user.access_token,
            'refresh_token': user.refresh_token,
        }


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'access_token',)
        read_only_fields = ('access_token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
