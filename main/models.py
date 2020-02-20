from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from rest_framework.permissions import BasePermission


class User(AbstractUser):
    objects = UserManager()


class Type(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True)
    level = models.IntegerField(default=0)
    # employee = models.ManyToManyField(Employee)
    type = models.ForeignKey(Type, on_delete=models.CASCADE,null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Employee(models.Model):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    skinname = models.CharField(max_length=150)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.name


#Black list
class BlackListedToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        unique_together = ("token", "user")

