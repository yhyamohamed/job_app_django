from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from rest_framework import status, routers, serializers, viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import CompanyCreationSerializer, DeveloperCreationSerializer, UserSerializer
from ...models import User


@api_view(['POST'])
@permission_classes([])
def company_sign_up(request):
    serializer = CompanyCreationSerializer(data=request.data)
    response = {'data': None, 'status': status.HTTP_201_CREATED}
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**response)


@permission_classes([])
class Users(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([])
class User(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([])
@api_view(['DELETE'])
def delete_user(request, id):
    res = User.objects.get(pk=id).delete()
    return Response(data={'response', 'Entry deleted'}, status=status.HTTP_204_NO_CONTENT)
