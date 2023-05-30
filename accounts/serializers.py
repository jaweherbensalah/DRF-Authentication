from django.contrib.auth.models import User, Group
from rest_framework import serializers
from social_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'firstname', 'lastname']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'
