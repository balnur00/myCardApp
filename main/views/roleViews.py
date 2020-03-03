from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from main.serializers.serializers import *
from rest_framework.response import Response



#ROLE VIEWS
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (AllowAny,)