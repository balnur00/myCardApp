from rest_framework import serializers
from main.models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)
    first_name = models.CharField()
    last_name = models.CharField()
    is_staff = models.BooleanField(default=True)
    # employees = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Role
        fields = ('id', 'name')


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    level = serializers.IntegerField(default=0)
    # photo = serializers.ImageField(required=False)

    class Meta:
        model = Skill
        fields = ('id', 'name', 'level')


class TypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Type
        fields = ('id', 'name')


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    skinname = serializers.CharField(required=True)
    # photo = serializers.IntegerField(default=0)
    # boss_id = UserSerializer(read_only=True)
    # role_id = serializers.RelatedField(source='role', read_only=True)
    # boss = serializers.SlugRelatedField(slug_field='username', read_only=True)
    role = serializers.SlugRelatedField(slug_field='name', read_only=True)
    skill = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'skinname', 'role', 'skill')

