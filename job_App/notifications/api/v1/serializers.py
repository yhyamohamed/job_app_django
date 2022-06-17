from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
        model = Notification
