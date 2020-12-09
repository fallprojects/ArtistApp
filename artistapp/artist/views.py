from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from artist import services

from rest_framework.decorators import action, api_view
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



@api_view(['GET','POST'])
def commentView(request,content_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(content_id=content_id)
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        try:
            content = Content.objects.get(id=content_id)
            comment = Comment(content=content)
        except Content.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
