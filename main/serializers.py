from rest_framework import serializers
from main.models import *


class BossSerializer(serializers.ModelSerializer):
    # queryset = Employee.objects.all()
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    # photo = serializers.ImageField(required=False)
    # employees = serializers.RelatedField(many=True, queryset=queryset)

    class Meta:
        model = Boss
        fields = ('id', 'name', 'username')


class EmployeeSerializer(serializers.ModelSerializer):
    # queryset = Skill.objects.all()
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    # photo = serializers.IntegerField(default=0)
    # skills = serializers.RelatedField(many=True, queryset=queryset)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'username', 'skills')


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    points = serializers.IntegerField(default=0)
    # photo = serializers.ImageField(required=False)


    class Meta:
        model = Skill
        fields = ('id', 'name', 'points')