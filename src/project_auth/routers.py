from rest_framework import routers
from django.urls import path, include

from .views import  Register, Celery

router = routers.DefaultRouter()

urlpatterns = [
    # path('api/', include(router.urls)),
    path('register/', Register.as_view(), name="register"),      
    path('test/', Celery.as_view(), name="celery"),      
]