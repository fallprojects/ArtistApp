from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, viewsets, views, status
from .serializers import *

# Create your views here.

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ProfileRegisterView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


