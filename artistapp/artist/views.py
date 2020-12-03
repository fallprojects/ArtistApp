from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from artist import services

from rest_framework.decorators import action
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, viewsets, views, status
from .serializers import *

# Create your views here.

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ProfileRegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request':request}
                                           )
        if not serializer.is_valid():
            return Response({'User not found'})
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
