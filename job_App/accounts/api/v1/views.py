from django.core.exceptions import ObjectDoesNotExist
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import status, routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout






@api_view(['POST'])
def logout(self, request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass

    logout(request)
    return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
