from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('uuid', 'username','password', 'email','first_name',
         'last_name', 'city', 'state', 'neighborhood', 'street', 'categories')