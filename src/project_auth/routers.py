from rest_framework import routers
from .views import Register

router = routers.DefaultRouter()

router.register(r'register', Register)

urlpatterns = router.urls