from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import NotificationSerializer
from ...models import Notification


@api_view(['GET'])
def notification_list(request, id):
    notifications_object = Notification.objects.all()
    print(notifications_object)
    serializer = NotificationSerializer(notifications_object, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
