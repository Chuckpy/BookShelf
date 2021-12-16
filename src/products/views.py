from .models import Products
from .serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.mixins import (CreateModelMixin, 
                                    ListModelMixin,
                                    UpdateModelMixin,
                                    RetrieveModelMixin,
                                    DestroyModelMixin
                                    )   
from rest_framework.viewsets import GenericViewSet
from rest_framework import status


class ProductList(GenericViewSet,ListModelMixin):

    permission_classes = [AllowAny]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer 
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['sub_category', ]
    search_fields = ['name', 'sub_category__name', 'sub_category__category__name']


class ProductCreate(GenericViewSet,CreateModelMixin):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer


class ProductUpdate(GenericViewSet,UpdateModelMixin, DestroyModelMixin):
    lookup_field='slug'
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        
        if serializer.data.get('owner') == request.user.id:
            return Response(serializer.data)
        else :
            return JsonResponse({'success':False, 'message':'usuario não autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
            


class ProductDetail(GenericViewSet,RetrieveModelMixin):
    lookup_field='slug'
    permission_classes = [AllowAny]
    queryset=Products.objects.all()
    serializer_class= ProductSerializer
