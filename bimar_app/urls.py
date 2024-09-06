from django.urls import path
from .views import *

urlpatterns = [
    path('bimar/', ListCreateBimar.as_view()),
    path('khedmat/', ListCreatekhedmat.as_view()),
    path('nobat/', ListCreateNobat.as_view()),
    path('nobat/<int:pk>/', RetrieveUpdateDestroyNobat.as_view()),
    path('pardakht/', ListPardakht.as_view())
]