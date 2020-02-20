from rest_framework import generics
from main.serializers.serializers import *


#Type VIEWS
class TypeListCreate(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer