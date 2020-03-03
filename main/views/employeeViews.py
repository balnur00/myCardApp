from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework import generics, status

from main.filters import EmployeeFilter
from main.serializers.serializers import *
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# from rest_framework.filters import SearchFilter, OrderingFilter

# EMPLOYEE VIEWS

# List
class EmployeeList(generics.ListAPIView):
    filter_backends = [SearchFilter]
    search_fields = ['name', 'surname']

    # filter_class = EmployeeFilter

    def get_queryset(self):
        # print(type(self.request.auth))
        return Employee.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        return EmployeeSerializer


# Create
class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# list one employee : delete or update
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        print(Employee.objects.filter(id=self.kwargs['pk']))
        queryset = Employee.objects.filter(id=self.kwargs['pk'])
        return queryset

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', ])
def retrieve_employee(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"status": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND)
    try:
        employee_skills = employee.skills.values()
    except ObjectDoesNotExist:
        return Response({"status": "This employee does not have skills"}, status=status.HTTP_404_NOT_FOUND)
    for skill in employee_skills:
        employee.points += 1  # TODO skill.level
        employee.save()
        serializer = EmployeeSerializer(employee)
    return Response(serializer.data)
