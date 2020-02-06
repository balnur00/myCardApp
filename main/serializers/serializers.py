from rest_framework import serializers
from main.models import *


class BossSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = models.CharField()
    last_name = models.CharField()
    # name = serializers.CharField(required=True)
    # surname = serializers.CharField(required=True)
    # skinname = serializers.CharField(required=True)
    # photo = serializers.ImageField(required=False)

    class Meta:
        model = Boss
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = SoftSkill
        fields = ('id', 'name')


class SoftSkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    level = serializers.IntegerField(default=0)
    # photo = serializers.ImageField(required=False)

    class Meta:
        model = SoftSkill
        fields = ('id', 'name', 'level')


class HardSkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    level = serializers.IntegerField(default=0)
    # photo = serializers.ImageField(required=False)

    class Meta:
        model = HardSkill
        fields = ('id', 'name', 'level')


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    skinname = serializers.CharField(required=True)
    # photo = serializers.IntegerField(default=0)
    # boss_id = serializers.RelatedField(source='boss', read_only=True)
    # role_id = serializers.RelatedField(source='role', read_only=True)
    boss_id = serializers.IntegerField(source='boss')
    role_id = serializers.IntegerField(source='role')
    softSkill = SoftSkillSerializer(many=True)
    hardSkill = HardSkillSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'skinname', 'boss_id', 'role_id', 'softSkill', 'hardSkill')

