from rest_framework import routers
from .views import (ProductList,
                    ProductCreate,
                    ProductUpdate,
                    ProductDetail,
                    ProductDelete,)

router = routers.DefaultRouter()

router.register(r"", ProductList)
router.register(r"create", ProductCreate)
router.register(r"update", ProductUpdate, basename="products-update")
router.register(r"delete", ProductDelete, basename="products-delete")
router.register(r"detail", ProductDetail, basename="products-detail")

urlpatterns = router.urls