from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import User

User = get_user_model()


class CompanyCreationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        fields = ('username', 'email', 'password', 'password_confirmation', 'address', 'user_type', 'is_active')
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'address': {'required': True},
            'user_type': {'required': True},
        }


class DeveloperCreationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        fields = ('username', 'email', 'password', 'password_confirmation', 'gender', 'user_type', 'is_active')
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'gender': {'required': True},
            'user_type': {'required': True},
        }


def create(self, validated_data):
    if self.validated_data.get('password') != self.validated_data.get('password_confirmation'):
        raise serializers.ValidationError('Password confirmation does not match')

    validated_data.pop('password')
    validated_data.pop('password_confirmation')
    user = User(**validated_data)
    user.set_password(self.validated_data.get('password'))
    user.is_active = False
    user.save()
    return user


CompanyCreationSerializer.create = create
DeveloperCreationSerializer.create = create


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=User

