from rest_framework import serializers
from main.models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    first_name = models.CharField()
    last_name = models.CharField()
    is_staff = models.BooleanField(default=True)
    # employees = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = User
        unique_together = ['first_name', 'last_name']
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_staff')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Role
        fields = ('id', 'name')


class TypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Type
        fields = ('id', 'name')


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    level = serializers.IntegerField(default=0)
    has_changed = serializers.BooleanField(default=False)
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    type_id = serializers.IntegerField()
    # photo = serializers.ImageField(required=False)

    class Meta:
        model = Skill
        fields = ('id', 'name', 'level', 'type', 'type_id', 'has_changed')


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    skinname = serializers.CharField(required=True)
    role = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # image = serializers.ImageField(required=False)
    skills = SkillSerializer(required=False, many=True, read_only=True)
    points = serializers.IntegerField()
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Employee
        unique_together = ['name', 'surname']
        fields = ('id', 'name', 'surname', 'skinname', 'role', 'skills', 'created_by', 'photo', 'points')


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField()
    employee_id = serializers.IntegerField()

    class Meta:
        model = Image
        fields = ('id', 'url', 'employee_id')


class BlackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackListedToken
        fields = ('__all__')

