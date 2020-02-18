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
