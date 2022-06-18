from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import User, Tag

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
        fields = ('username', 'email', 'password', 'password_confirmation', 'gender', 'user_type', 'is_active', 'tags')
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'gender': {'required': True},
            'user_type': {'required': True},
            'tags': {'required': True}
        }


def create(self, validated_data):
    if self.validated_data.get('password') != self.validated_data.get('password_confirmation'):
        raise serializers.ValidationError('Password confirmation does not match')

    validated_data.pop('password')
    validated_data.pop('password_confirmation')
    if 'tags' in validated_data:
        tags = validated_data.pop('tags')
    user = User(**validated_data)
    user.set_password(self.validated_data.get('password'))
    type = self.validated_data.get('user_type')
    if type == 'recruiter':
        user.is_active = False
    elif type == 'developer':
        user.is_active = True
    user.save()
    if 'tags' in locals():
        user.tags.set(tags)
    return user


CompanyCreationSerializer.create = create
DeveloperCreationSerializer.create = create


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tag


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User




class UserSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        # fields = '__all__'
        exclude = ['password']
        model = User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ['password']
        model = User
        depth = 1
