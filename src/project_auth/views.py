from .models import BaseUser
from .serializers import BaseUserSerializer

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.mixins import CreateModelMixin   
from rest_framework.viewsets import GenericViewSet

class Register(GenericViewSet, CreateModelMixin):
    permission_classes= [AllowAny]
    queryset=BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    

# class Login(): 


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

