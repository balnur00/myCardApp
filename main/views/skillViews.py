from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from main.serializers.serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


@api_view(['post',])
def increase_level(request,pk,pk2):
    # Input: another_user_id, skill_id
    # 1. Choose a person
    try:
        employee = Employee.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"status": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND)
    # 2. Choose a skill
    try:
        skill = employee.skills.get(id=pk2)
    except ObjectDoesNotExist:
        return Response({"status": "Skill does not exist"}, status=status.HTTP_404_NOT_FOUND)
    skill.level +=1
    skill.save()
    return Response({"status": "ura"})


@api_view(['post',])
def dec_level(request,pk,pk2):
    try:
        employee = Employee.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"status": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND)
    try:
        skill = employee.skills.get(id=pk2)
    except ObjectDoesNotExist:
        return Response({"status": "Skill does not exist"}, status=status.HTTP_404_NOT_FOUND)
    skill.level -=1
    skill.save()
    return Response({"status": "ura"})


#SKILL VIEWS
class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    # def list(self, request):
    #     queryset = self.objects.all()
    #     serializer = SkillSerializer(self.get_queryset(), many=True)
    #     return Response(serializer.data)


class SkillCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

#
# class SkillUpdateLevelUp(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer
#
#     def get_queryset(self):
#         return Skill.objects.filter(id=self.kwargs['pk'])
#
#     def patch(self, request, *args, **kwargs):
#         model = get_object_or_404(Skill, id=self.kwargs['pk'])
#         data = {"level": model.level+1}
#         serializer = SkillSerializer(model, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SkillUpdateLevelDown(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer
#
#     def get_queryset(self):
#         return Skill.objects.filter(id=self.kwargs['pk'])
#
#     def patch(self, request, *args, **kwargs):
#         model = get_object_or_404(Skill, id=self.kwargs['pk'])
#         if model.level>0 :
#             data = {"level": model.level-1}
#             serializer = SkillSerializer(model, data=data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_200_OK)
