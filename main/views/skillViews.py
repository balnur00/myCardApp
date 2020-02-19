from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics
from main.serializers.serializers import *
from rest_framework.response import Response



#SKILL VIEWS
class SkillCreateList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        return Skill.objects.filter(id=self.kwargs['pk'])


