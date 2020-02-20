# from main.models import *
# from main.serializers import *
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.authtoken.models import Token
#
# from main.serializers.serializers import UserSerializer
#
#
# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         User.objects.create_user(
#             username=serializer.data['username'],
#             email=serializer.data['email'],
#             password=serializer.initial_data['password']
#         )
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['POST', ])
# def login(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data.get('user')
#     token, created = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key})
#
#
# @api_view(['POST', ])
# def logout(request):
#     request.auth.delete()
#     return Response(status=status.HTTP_200_OK)

from rest_framework.permissions import BasePermission
from main.models import BlackListedToken
from rest_framework import generics

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


# class UserLogout(generics.RetrieveUpdateDestroyAPIView):

