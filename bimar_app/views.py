from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser


class ListCreateBimar(ListCreateAPIView):
    queryset = Bimar.objects.all()
    serializer_class = BimarSerializer
    permission_classes = [IsAdminUser]


class
