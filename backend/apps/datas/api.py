from rest_framework import generics
from .models import Industry, Employes
from .serializers import DatasSerializer

class IndustryList(generics.ListAPIView):
    queryset = Industry.objects.filter(active=True).order_by('id')
    serializer_class = DatasSerializer

class EmployesList(generics.ListAPIView):
    queryset = Employes.objects.filter(active=True).order_by('id')
    serializer_class = DatasSerializer