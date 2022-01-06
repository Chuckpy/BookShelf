from rest_framework import serializers
from .models import BaseUser

class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ('id', 'username','password', 'email','first_name',
         'last_name', 'city', 'state', 'neighborhood', 'street', 'categories')