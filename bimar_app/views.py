from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from user_app.permissins import *


class ListCreateBimar(ListCreateAPIView):
    queryset = Bimar.objects.all()
    serializer_class = BimarSerializer
    permission_classes = [IsAdminUser]


class ListCreatekhedmat(ListCreateAPIView):
    queryset = Khedmat.objects.all()
    serializer_class = KhedmatSerializer
    permission_classes = [IsAdminUser]
    
    

class ListCreateNobat(ListCreateAPIView):
    queryset = Nobat.objects.all()
    serializer_class = NobatSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['bimar__name']
    ordering_fields = ['date']
    filterset_fields = ['date']


class RetrieveUpdateDestroyNobat(RetrieveUpdateDestroyAPIView):
    queryset = Nobat.objects.all()
    serializer_class = NobatSerializer
    permission_classes = [IsAdminUser]


class ListPardakht(ListAPIView):
    queryset = Nobat.objects.all()
    serializer_class = PardakhtSerializer
    permission_classes = [IsSuperUser]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']