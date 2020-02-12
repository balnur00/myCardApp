from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from django.http import Http404
from main.serializers.serializers import *


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = (AllowAny, )
    # permission_classes = (IsAuthenticated,)

    # authentication_classes = (BasicAuthentication, )


class BossCreate(generics.ListCreateAPIView):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer
    # permission_classes = (AllowAny, )


class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = (IsAuthenticated, )
    # permission_classes = (AllowAny, )


class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # permission_classes = (AllowAny, )


class SoftSkillCreateList(generics.ListCreateAPIView):
    queryset = SoftSkill.objects.all()
    serializer_class = SoftSkillSerializer
    # permission_classes = (AllowAny, )


class HardSkillCreateList(generics.ListCreateAPIView):
    queryset = HardSkill.objects.all()
    serializer_class = HardSkillSerializer
    permission_classes = (AllowAny, )


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        print(Employee.objects.filter(id=self.kwargs['pk']))
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset

