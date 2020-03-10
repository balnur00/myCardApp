from main.models import Employee
import django_filters as df
from django_filters import rest_framework as filters


class InListFilter(df.Filter):
    def filter(self, qs, value):
        if value:
            return qs.filter(**{self.field_name+'__in': value.split(',')})
        return qs


class NumberInFilter(df.rest_framework.BaseInFilter, df.rest_framework.NumberFilter):
    pass


class EmployeeFilter(df.FilterSet):
    role = InListFilter(field_name='role__name')
    # points_gte = df.NumberFilter(field_name='points', lookup_expr='gte')
    # skill_type = df.ModelMultipleChoiceFilter(
    #     field_name='skills__type__name',
    #     to_field_name='type',
    #     lookup_expr='in',
    #     queryset=Employee.objects.all(),
    # )
    # skills_name = df.ModelMultipleChoiceFilter(
    #     field_name='skills__name',
    #     to_field_name='name',
    #     lookup_expr='in',
    #     queryset=Employee.objects.all(),
    # )
    skill_type = NumberInFilter(field_name='skills__type', lookup_expr='in')

    class Meta:
        model = Employee
        fields = ('name', 'role', 'skills', 'skills__name', 'skills__type__name', )


