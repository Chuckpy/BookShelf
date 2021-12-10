from .models import Products
from .serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.mixins import (CreateModelMixin, 
                                    ListModelMixin,
                                    UpdateModelMixin,
                                    RetrieveModelMixin,
                                    DestroyModelMixin
                                    )   
from rest_framework.viewsets import GenericViewSet


class ProductList(GenericViewSet,ListModelMixin):

    permission_classes = [AllowAny]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer 
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['sub_category', ]
    search_fields = ['name', 'sub_category', 'sub_category__category']


class ProductCreate(GenericViewSet,CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer


class ProductUpdate(GenericViewSet,UpdateModelMixin):
    lookup_field='slug'
    permission_classes = [IsAuthenticated]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer


class ProductDetail(GenericViewSet,RetrieveModelMixin):
    lookup_field='slug'
    permission_classes = [IsAuthenticated]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer


class ProductDelete(GenericViewSet,DestroyModelMixin):
    lookup_field='slug'
    permission_classes = [IsAuthenticated]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer

