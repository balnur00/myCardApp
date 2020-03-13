from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from main.serializers.serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


@api_view(['post',])
def increase_level(request, pk, pk2):
    try:
        employee = Employee.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"status": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND)
    try:
        skill = employee.skills.get(id=pk2)
    except ObjectDoesNotExist:
        return Response({"status": "Skill does not exist"}, status=status.HTTP_404_NOT_FOUND)
    skill.level += 1
    skill.save()
    return Response({"status": "ura"})


@api_view(['post',])
def dec_level(request, pk, pk2):
    try:
        employee = Employee.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"status": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND)
    try:
        skill = employee.skills.get(id=pk2)
    except ObjectDoesNotExist:
        return Response({"status": "Skill does not exist"}, status=status.HTTP_404_NOT_FOUND)
    skill.level -= 1
    skill.save()
    return Response({"status": "ura"})


#SKILL VIEWS
class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

