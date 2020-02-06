from django.db import models
from django.contrib.auth.models import User


class Boss(User):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    # name = models.CharField(max_length=200)
    # surname = models.CharField(max_length=200)
    # skinname = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Boss'
        verbose_name_plural = 'Bosses'


class Role(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name


class HardSkill(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.name


class SoftSkill(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Employee(models.Model):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    skinname = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, related_name="employees")
    boss = models.ForeignKey(Boss, on_delete=models.DO_NOTHING, related_name="employees")
    softSkill = models.ManyToManyField(SoftSkill, related_name="employees")
    hardSkill = models.ManyToManyField(HardSkill, related_name="employees")

    objects = models.Manager()

    def __str__(self):
        return self.name
