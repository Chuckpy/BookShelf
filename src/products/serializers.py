from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):

    class Meta :
        model = Products
        fields = ('id', 'name','slug', 'description', 'short_description', 
        'product_information', 'stock', 'available', 
        'sub_category', 'owner', 'created', 'updated')
        