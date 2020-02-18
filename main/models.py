from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from rest_framework.permissions import BasePermission
# from django.core.exceptions.ObjectDoesNotExist import DoesNotExist
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

#
# class UserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""
#
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         """Create and save a regular User with the given email and password."""
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)


class Boss(User):
    # skinname = models.CharField(max_length=200)
    objects = UserManager()
    # email = models.EmailField(_('email address'), unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    # username = None

    class Meta:
        verbose_name = 'Boss'
        verbose_name_plural = 'Bosses'


class Role(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()


class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="skills")
    objects = models.Manager()


class Employee(models.Model):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    skinname = models.CharField(max_length=200, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="employee")
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE, related_name="employees")
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="employee")

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