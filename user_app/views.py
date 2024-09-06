from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissins import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass


