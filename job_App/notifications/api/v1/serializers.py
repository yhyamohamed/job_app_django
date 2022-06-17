from rest_framework import serializers

from accounts.api.v1.serializers import UserSerializer

from ...models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    sent_to = UserSerializer()

    class Meta:
        fields = '__all__'
        model = Notification
        depth = 1
