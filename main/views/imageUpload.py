from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import cloudinary
import cloudinary.uploader as uploader
from secrets import token_urlsafe

from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from main.models import Employee, Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader

from main.serializers.serializers import ImageSerializer


class ImageUploadView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def post(self, request, pk):
        try:
            emp = Employee.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({"status": "Employee does not exist"}, status=status.HTTP_404_NOT_FOUND)

        file = request.data.get('picture')
        res = cloudinary.uploader.upload(file)

        image = Image(
            url=res['secure_url'],
            employee=emp
        )
        image.save()

        return Response({
            'status': 'success',
            'data': res,
        }, status=201)


class ImageView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)