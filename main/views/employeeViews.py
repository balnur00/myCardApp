from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from main.serializers.serializers import *
from rest_framework.response import Response


#EMPLOYEE VIEWS

#List
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

#Create
class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#list one employee : delete or update
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        print(Employee.objects.filter(id=self.kwargs['pk']))
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset

