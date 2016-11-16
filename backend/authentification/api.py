from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import AuthTokenSerializer, UserSerializer
from .models import User
from rest_framework import status

class ObtainAuthUser(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class VerificationEmail(APIView):
    """Check if email exist """
    def post(self, request):
        if 'email' in request.data:
            if not User.objects.filter(email=request.data['email']).exists():
                return Response({'email': True})

        return Response({'email' : False}, status=status.HTTP_401_UNAUTHORIZED)


class ObtainAuthToken(APIView):
    """
    # Api auth.
    Use to retreive token authentication for a user.
    Only post requests are allowed.

    Needed params:
    * email
    * password

    response: {token: user_token}
    """

    def post(self, request):
        """Try to retreive user token."""
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})