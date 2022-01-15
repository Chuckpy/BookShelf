from rest_framework import routers
from .views import  Register
from django.urls import path, include

router = routers.DefaultRouter()

# router.register(r'register', Register)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('register/', Register.as_view(), name="register"),    
]