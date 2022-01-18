from django.urls import include, path
from rest_framework import routers
from .views import (ProductList,
                    ProductCreate,
                    ProductUpdate,
                    ProductDetail,
)

router = routers.DefaultRouter()

router.register(r"", ProductList)
router.register(r"create", ProductCreate)
router.register(r"update", ProductUpdate, basename="products-update")
router.register(r"detail", ProductDetail, basename="products-detail")

urlpatterns = [
    path(r"", include(router.urls))
]