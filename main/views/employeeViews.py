from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from main.filters.employeeFilter import EmployeeFilter
from main.serializers.serializers import *
from rest_framework.response import Response
from django_filters import rest_framework as filters


# List
class EmployeeList(generics.ListAPIView):
    filter_backends = (SearchFilter, filters.DjangoFilterBackend, )
    search_fields = ('name', 'surname',)
    filter_class = EmployeeFilter
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # @swagger_auto_schema(responses={200: EmployeeSerializer(many=True)})
    # def get(self, request):
    #     return Response('OK')


# Create
class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    # @swagger_auto_schema(operation_description="description")
    # def post(self, request):
    #     return Response('Employee')


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
