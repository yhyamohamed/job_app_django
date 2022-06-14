from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from rest_framework import status, routers, serializers, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView,ListAPIView
from accounts.models  import User
from .serializers import ProfileSerializer


from .serializers import CompanyCreationSerializer


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


@api_view(['GET'])
@permission_classes([])
def profiles(request):
    profile_object=User.objects.all()
    serializer=ProfileSerializer(profile_object,many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def show(request,id):
    profile_object=User.objects.filter(pk=id)
    serializer=ProfileSerializer(profile_object,many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


