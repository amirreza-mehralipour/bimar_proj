from rest_framework.serializers import ModelSerializer
from .models import *

class BimarSerializer(ModelSerializer):
    class Meta:
        model = Bimar
        fields = '__all__'


class KhedmatSerializer(ModelSerializer):
    class Meta:
        model = Khedmat
        fields = '__all__'


class NobatSerializer(ModelSerializer):
    class Meta:
        model = Nobat
        fields = ['bimar', 'date', 'khedmat__name']


class PardakhtSerializer(ModelSerializer):
    class Meta:
        model = Nobat
        fields = "__all__"