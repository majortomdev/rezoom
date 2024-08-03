from rest_framework import serializers
from .models import User, UrlObject

class UserSerialiazer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ['id','username','email','name','password']
            extra_kwargs = {'password':{'write_only:True'}}
    def create(self, validated_data):
            user = User(email=validated_data['email'],
                      username = validated_data['username'],
                      name = validated_data['name']
                      )
            user.set_password(validated_data['password'])
            user.save()
            return user
class UrlobjectSerializer(serializers.ModelSerializer):
       class Meta:
            model = UrlObject
            fields = ['id','active','url','user']