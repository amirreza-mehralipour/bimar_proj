from rest_framework.generics import ListCreateAPIView
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser


class ListCreateBimar(ListCreateAPIView):
    queryset = Bimar.objects.all()
    serializer_class = BimarSerializer
    permission_classes = [IsAdminUser]


class listcreatedkhedmat(ListCreateAPIView):
    queryset = Khedmat.objects.all()
    serializer_class = KhedmatSerializer
    permission_classes = [IsAdminUser]
    
    

class listcreatedNobat(ListCreateAPIView):
    queryset = Nobat.objects.all()
    serializer_class = NobatSerializer
    permission_classes = [IsAdminUser]
    