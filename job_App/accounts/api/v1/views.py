from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from rest_framework import status, routers, serializers, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from .serializers import CompanyCreationSerializer, DeveloperCreationSerializer


@api_view(['POST'])
@permission_classes([])
def sign_up(request):
    if request.data.get('user_type') == 'recruiter':
        serializer = CompanyCreationSerializer(data=request.data)
    elif request.data.get('user_type') == 'developer':
        serializer = DeveloperCreationSerializer(data=request.data)
    else:
        return Response({'message': 'Unsupported user type', 'status': status.HTTP_400_BAD_REQUEST})

    response = {'data': None, 'status': status.HTTP_201_CREATED}
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**response)
