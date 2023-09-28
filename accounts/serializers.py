from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import User, Person


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'firstname', 'lastname']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'