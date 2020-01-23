from django.db import models


class Boss(models.Model):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    # employees = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, default=None)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Employee(models.Model):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    # skills = models.ForeignKey(Skill, on_delete=models.DO_NOTHING, default=None)
    boss = models.ForeignKey(Boss, on_delete=models.DO_NOTHING, related_name="employees", default=2)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Skill(models.Model):
    # photo = models.ImageField(upload_to='media', default=None, null=True)
    name = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name="skills", null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name











