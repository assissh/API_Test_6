import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilizers import UserSerilizers
from rest_framework import status
from . import models
from . import serilizers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from . import permissions
# Create your views here.
from rest_framework.parsers import JSONParser
class User(APIView):

    def get(self,request):

        User_get = [
            'This the the user get API'
        ]
        return Response({'message':'GET_API','User_get':User_get})

    def post(self,request):

        serializer = UserSerilizers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hey {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serilizers.Userprofileserilizer
    queryset = models.User_Profile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self,request):

        return ObtainAuthToken().post(request)

class UserProfileFeed(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serilizers.ProfileFeedserializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)






    # def get_1(self,request):



    #     User_get_1 = UserSerilizers(data=request.data)
    #     if User_get_1.is_valid():
    #         return Response({'GET_User':User_get_1})
    # def post(self,request):
    #     serilizer = UserSerilizers(data=request.data)
    #     if serilizer.is_valid():
    #         name = serilizer.data.get('name')
    #         message = 'Hello {0}'.format(name)
    #         return Response({'message':message})
