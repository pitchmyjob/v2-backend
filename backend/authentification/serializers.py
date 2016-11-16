from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions, serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class AuthTokenSerializer(serializers.Serializer):
    """
    Manage authentication for the API
    """
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

    def validate(self, attrs):
        user = authenticate(email=attrs.get('email'), password=attrs.get('password'))
        if user:
            if not user.is_active:
                msg = 'User account is disabled.'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Unable to log in with provided email and password.'
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs