from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from rest_framework.permissions import BasePermission


class User(AbstractUser):
    objects = UserManager()


class Role(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="skills")
    objects = models.Manager()

    def __str__(self):
        return self.name


class Employee(models.Model):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="employee")
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="employee")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.name


#Black list migrate needed
class BlackListedToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        unique_together = ("token", "user")


class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        is_allowed_user = True
        token = request.auth.decode("utf-8")
        try:
            is_blackListed = BlackListedToken.objects.get(user=user_id, token=token)
            if is_blackListed:
                is_allowed_user = False
        except BlackListedToken.objects.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user