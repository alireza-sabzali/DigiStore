from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, request):
        user = User(username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user
