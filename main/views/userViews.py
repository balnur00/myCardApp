from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from main.serializers.serializers import *
from rest_framework.response import Response


#BOSS VIEWS
class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

