from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import User

User = get_user_model()


class CompanyCreationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        fields = ('username', 'email', 'first_name', 'password', 'password_confirmation', 'address')
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'address': {'required': True},
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username')
        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirmation'):
            raise serializers.ValidationError('pass dont match')

        user.set_password(self.validated_data.get('password'))
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=User
