from rest_framework import serializers
from . import models
from rest_framework import permissions

class UserSerilizers(serializers.Serializer):
    name = serializers.CharField(max_length=20)

class Userprofileserilizer(serializers.ModelSerializer):
    class Meta:
        model = models.User_Profile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = models.User_Profile(
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileFeedserializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status','created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

