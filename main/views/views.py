from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from main.serializers.serializers import *
from rest_framework.response import Response


#EMPLOYEE VIEWS
class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        print(type(self.request.auth))
        return Employee.objects.filter(boss_id=self.request.user)
    # queryset = TaskList.objects.all()
    # serializer_class = TaskListSerializer

    def get_serializer_class(self):
        return EmployeeSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)


class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        print(Employee.objects.filter(id=self.kwargs['pk']))
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset


#BOSS VIEWS
class BossCreate(generics.ListCreateAPIView):
    queryset = Boss.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AllowAny, )


#ROLE VIEWS
class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


#SKILL VIEWS
class SkillCreateList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        return Skill.objects.filter(id=self.kwargs['pk'])


