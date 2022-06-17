from django.contrib.auth import get_user_model, logout
# from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.views.generic import CreateView
from rest_framework import status, routers, serializers, viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView, ListAPIView

from .serializers import ProfileSerializer

from .serializers import CompanyCreationSerializer, DeveloperCreationSerializer, UserSerializer, TagSerializer
from django.core.exceptions import ObjectDoesNotExist
from ...models import User,Tag


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


class LogUserIn(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        serializer = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': serializer.data})


@api_view(['POST'])
@permission_classes([])
def get_user_from_token(request):
    user = Token.objects.get(key=request.data['token']).user
    serializer = UserSerializer(user)
    return Response({'id': user.id, 'user': serializer.data})


@api_view(['GET'])
@permission_classes([])
def profiles(request):
    profile_object = User.objects.all()
    serializer = ProfileSerializer(profile_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([])
def show_profile(request, id):
    profile_object = User.objects.filter(pk=id)
    serializer = ProfileSerializer(profile_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
@permission_classes([])
def update_profile(request, id):
    if request.user.id == id:
        profile_user = User.objects.filter(pk=id).first()
        serializer = UserSerializer(instance=profile_user, data=request.data)
        if request.method == 'PATCH':
            serializer = UserSerializer(instance=profile_user, data=request.data, partial=True)
        response = {'data': None, 'status': status.HTTP_201_CREATED}
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
        else:
            print('not found')
            response['data'] = serializer.errors
            response['status'] = status.HTTP_400_BAD_REQUEST
        return Response(**response)
    else:
        profile_user = User.objects.filter(pk=id)
        serializer = ProfileSerializer(profile_user, many=True)
        return Response(data={'cant edit this profile'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([])
def delete_profile(request, id):
    deleted_item = User.objects.get(pk=id).delete()
    return Response(data={'response', 'Entry deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([])
def list_tags(request):
    tag_object = Tag.objects.all()
    serializer = TagSerializer(tag_object, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def log_user_out(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    logout(request)
    return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)

# request.user.id
