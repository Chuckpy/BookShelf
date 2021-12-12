from .models import BaseUser
from .serializers import BaseUserSerializer

from rest_framework.permissions import AllowAny
from rest_framework.mixins import CreateModelMixin   
from rest_framework.viewsets import GenericViewSet

class Register(GenericViewSet, CreateModelMixin):
    permission_classes= [AllowAny]
    queryset=BaseUser.objects.all()
    serializer_class = BaseUserSerializer
