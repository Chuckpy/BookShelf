from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Products, OpenSearch

class ProductSerializer(serializers.ModelSerializer):
    
    links = serializers.SerializerMethodField()

    class Meta :
        model = Products
        fields = ( 'id','name','slug', 'description', 'short_description', 
        'product_information', 'stock', 'available', 
        'sub_category', 'owner', 'registration', 'update','links')
    
    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('products-detail-detail', kwargs={'slug': obj.slug}, request=request),            
            'update': reverse('products-update-detail', kwargs={'slug': obj.slug}, request=request)
        }


class OpenSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpenSearch
        fields = ('own_product', 'like_list','dislike_list', 'match')

