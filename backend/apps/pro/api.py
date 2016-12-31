from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import SignUpProSerializer, ProSerializer
from rest_framework.response import Response
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from backend.apps.pro.models import Pro

class SignUpPro(APIView):

    def post(self, request):
        serializer = SignUpProSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class retreiveUpdatePro(generics.RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ProSerializer

    def get_object(self):
        return self.request.user.pro