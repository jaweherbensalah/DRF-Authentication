from accounts.serializers import UserSerializer
from django.contrib.auth import authenticate
from accounts.models import User
import os
import random
from rest_framework.exceptions import AuthenticationFailed


def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)

from rest_framework.response import Response
def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:
            username = User.objects.get(email=email).username
            email = User.objects.get(email=email).email
            old_user = User.objects.filter(email__exact=email).first()

            serializer = UserSerializer(old_user)
            return serializer.data

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': 'adminitration'}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        
        user.save()
        print("new user           :")

        new_user = authenticate(
            username=user.username, password='')
        print(new_user)
        serializer = UserSerializer(user)
        return serializer.data


