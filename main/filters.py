from django_filters import rest_framework as filters
from main.models import *


class EmployeeFilter(filters.Filter):
    name = filters.CharFilter(lookup_expr='contains')
    surname = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Employee
        fields = ('name', 'surname')