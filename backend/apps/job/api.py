from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import JobSerializer, JobQuestionSerializer
from .models import Job, JobQuestion
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import list_route
from rest_framework import generics
from backend.authentification.permissions import IsProPermission


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsProPermission)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        return self.request.user.pro.job_set.all()


class ListCreateJobQuestion(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsProPermission)
    serializer_class = JobQuestionSerializer

    def perform_create(self, serializer):
        serializer.save(job=Job.objects.get(id=self.kwargs['job']))

    def get_queryset(self):
        job = get_object_or_404(Job, id=self.kwargs['job'], pro=self.request.user.pro)
        return job.questions.all()


class RetrieveJobQuestion(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsProPermission)
    serializer_class = JobQuestionSerializer

    def get_object(self):
        return get_object_or_404(JobQuestion, id=self.kwargs['pk'], job__pro=self.request.user.pro, job=self.kwargs['job'])